def sift_down(array, i, size, swap_list):
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < size and array[left] < array[min_index]:
        min_index = left

    if right < size and array[right] < array[min_index]:
        min_index = right 

    if i != min_index:
        array[i], array[min_index] =  array[min_index], array[i]
        swap_list.append((i, min_index))
        sift_down(array, min_index, size, swap_list)

def build_heap(array):
    size = len(array)
    swap_list = []

    for i in range((size // 2) - 1, -1, -1):
        sift_down(array, i, size, swap_list)

    return swap_list

if __name__ == '__main__':
    n = int(input())
    string = input().split()
    output = map(int, string)
    array = list(output)
    # print(array)
    
    swaps = build_heap(array)

    print(len(swaps))   
    for x, y in swaps:
        print(x,' ', y) 