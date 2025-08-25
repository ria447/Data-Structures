def phone_book_operation():
    phone_book = {}
    output = []
    n = int(input())
    for i in range(n):

        query_parts = input().split()
        
        if query_parts[0]  == 'add':
            number, name = query_parts[1], query_parts[2]
            phone_book[number] = name
            
        
        elif query_parts[0] == 'find':
            find_result = phone_book.get(query_parts[1], 'not found')
            output.append(find_result)
        
        elif query_parts[0] == 'del':
            number = query_parts[1]
            phone_book.pop(number, None)
                
    for i in output:
       print(i)

if __name__ == '__main__':
    phone_book_operation()