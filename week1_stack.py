def stack_operation():
    stack = []
    max_stack = []
    queries = int(input())
    for i in range(queries):
        query = input().strip()

        query_parts = query.split()
        if query_parts[0]  == 'push':
            stack.append(int(query_parts[1])) 
            if len(max_stack) == 0:
                max_stack.append(int(query_parts[1]))
            elif int(query_parts[1]) >= max_stack[-1]:
                max_stack.append(int(query_parts[1]))
        elif query_parts[0]  == 'max':
            print(max_stack[-1])
        else:
            last_elestack = stack[-1]
            last_elemaxst = max_stack[-1]
            if len(stack) != 0:
                if last_elestack == last_elemaxst:
                    stack.pop()
                    max_stack.pop()
                else:
                    stack.pop()



if __name__ == '__main__':
    stack_operation()
        
