import sys
import threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
    
def is_bst_util(tree, node, min_val, max_val):
    if node == -1:              #yeh samjhna hai    
        return True 
    
    key, left, right = tree[node]

    if key < min_val or key > max_val:
        return False
    if left != -1 and tree[left][0] >= key:
        return False
    if right != -1 and tree[right][0] < key:
        return False
    
    return (is_bst_util(tree, left, min_val, key-1) and is_bst_util(tree, right, key, max_val))


def is_bst(tree):
    if len(tree) <= 1:
        return "CORRECT"
    
    if is_bst_util(tree, 0, float("-inf"), float("inf")):
        return "CORRECT"
    return "INCORRECT"

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