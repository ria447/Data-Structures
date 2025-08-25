def check_brackets(string):
    stack = []
    index = 0
    for char in string:
        index += 1
        if char in '([{': 
            stack.append((char, index))
        elif char in '}])':
            if len(stack) == 0:
                return index
            
            top, top_index = stack.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')') or (top == '{' and char != '}'):
                return index
            
    if len(stack) == 0:
        return 'Success'
    else:
        return stack[0][1] 

if __name__ == '__main__':
    string = input()
    output = check_brackets(string)
    print(output)

   