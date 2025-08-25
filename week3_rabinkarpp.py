def hashing_function(string, prime_number, x):
    hash = 0
    for i in range(len(string)-1, -1, -1):
        hash = (hash * x + ord(string[i])) % prime_number
    
    return hash 

def are_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def precompute_hashes(text, pattern_length, prime_number, multiplier):
    hashes = [0] * (len(text) - pattern_length + 1)
    # the for loop below is to create an array of length len(t) - len(p) +1
    # for _ in range(len(text) - pattern_length + 1):
    #     hashes.append(0) 

    i_start = len(text) - pattern_length
    i_end = len(text)
    substring = text[i_start:i_end]
    hashes[-1] = hashing_function(substring, prime_number, multiplier)

    # precompute (multiplier)^pattern_length for rolling
    y = 1
    for i in range(pattern_length):
        y = (y * multiplier) % prime_number
    
    # rolling hash backwards
    for i in range(len(text) - pattern_length -  1, -1, -1):
        hashes[i] = (multiplier * hashes[i+1] + ord(text[i]) - y * ord(text[i + pattern_length])) % prime_number
    return hashes 

    

def rabin_karp(text, pattern):
    prime_number = 1000000007
    x = 263
    len_p = len(pattern)
    # we will have to check if the pattern length is not greater than text length
    if len_p > len(text):
        return []

    positions = []
    pHash = hashing_function(pattern, prime_number, x)
    hashes = precompute_hashes(text, len_p, prime_number, x)


    for i in range(len(text)-len_p + 1):
        if pHash != hashes[i]:
            continue

        if text[i:i+len_p] == pattern:
                positions.append(i)

    return positions

if __name__ == '__main__':
    pattern = input().strip()
    text = input().strip()
    output = rabin_karp(text, pattern)

    length = len(output) 

    print(' '.join(map(str, output)))

    # for j in range(length):
    #     if j == length -1:
    #         print(output[j])
    #     else:
    #         print(output[j], end = ' ')