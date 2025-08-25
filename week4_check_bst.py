import sys
import threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size
    
def in_order_traversal(tree, parent = 0, result = None):
    if result is None:
        result = [] 
    if parent == -1:
        return
    
    in_order_traversal(tree, tree[parent][1], result)
    result.append(tree[parent][0])
    in_order_traversal(tree, tree[parent][2], result)

    return result

def is_bst(tree):
    if len(tree) <= 1:
        return "CORRECT"
    
    result = in_order_traversal(tree)

    for i in range(len(result)-1):
        if result[i] > result[i+1]:
            return "INCORRECT"
    return "CORRECT"

def main():
    n = int(input())
    lst = []
    for i in range(n):
        inputs = list(map(int, input().strip().split()))

        lst.append(inputs)
    output = is_bst(lst)
    print(output)

if __name__ == "__main__":
    threading.Thread(target=main).start()

    # sample_1 = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
    # sample_2 = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
    # sample_3 = []
    # sample_4 = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5,-1,-1]]
    # sample_5 = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1,-1,-1], [3,-1,-1], [5,-1,-1], [7,-1,-1]]
    # sample_6 = [[4, 1,-1], [2, 2, 3], [1,-1,-1], [5,-1,-1]]
    # print(is_bst(sample_1))
    # print(is_bst(sample_2))
    # print(is_bst(sample_3))
    # print(is_bst(sample_4))
    # print(is_bst(sample_5))
    # print(is_bst(sample_6))