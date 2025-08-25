import sys
import threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
    
def in_order_traversal(tree, parent = 0, result = None):
    if result is None:
        result = [] 
    if parent == -1:
        return
    
    in_order_traversal(tree, tree[parent][1], result)
    result.append(tree[parent][0])
    in_order_traversal(tree, tree[parent][2], result)

    return result

def pre_order_traversal(tree, parent = 0, result = None):
    if result is None:
        result = [] 
    if parent == -1:
        return
    
    result.append(tree[parent][0])
    pre_order_traversal(tree, tree[parent][1], result)
    pre_order_traversal(tree, tree[parent][2], result)

    return result

def post_order_traversal(tree, parent = 0, result = None):
    if result is None:
        result = [] 
    if parent == -1:
        return
    
    post_order_traversal(tree, tree[parent][1], result)
    post_order_traversal(tree, tree[parent][2], result)
    result.append(tree[parent][0])

    return result



def main():
    n = int(input())
    lst = []
    for i in range(n):
        inputs = list(map(int, input().strip().split()))

        lst.append(inputs)
    output_inorder = in_order_traversal(lst)
    output_preorder = pre_order_traversal(lst)
    output_postorder = post_order_traversal(lst)
    print(' '.join(map(str, output_inorder)))
    print(' '.join(map(str, output_preorder)))
    print(' '.join(map(str, output_postorder)))

if __name__ == "__main__":
    threading.Thread(target=main).start()

