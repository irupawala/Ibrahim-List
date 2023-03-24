''' pure storage buddy system bitmap
    Given a complete binary tree with nodes of values of either 1 or 0, the following rules always hold:
    (1) a node's value is 1 if and only if all its subtree nodes' values are 1
    (2) a leaf node can have value either 1 or 0
    Implement the following 2 APIs:
    set_bit(offset, length), set the bits at range from offset to offset+length-1
    clear_bit(offset, length), clear the bits at range from offset to offset+length-1
    
    i.e. The tree is like:
                 0
              /     \
             0        1
           /  \      /  \
          1    0    1    1
         /\   / \   / 
        1  1 1   0 1
        Since it's complete binary tree, the nodes can be stored in an array:
        [0,0,1,1,0,1,1,1,1,1,0,1] 
        
'''

'''
Refer Links

https://www.1point3acres.com/bbs/thread-300178-1-1.html
https://www.1point3acres.com/bbs/thread-297743-1-1.html
https://github.com/wolfsniper2388/Tech_Interviews/blob/master/others/buddy_bitmap.py
https://massivealgorithms.blogspot.com/2016/06/buttercola-buddy-system.html
'''

def setBitsRecursive(A, index):
    n = len(A)
    if index >= n: return 
    left_child = 2*index+1
    if left_child < n and A[left_child] == 0:
        A[left_child] = 1
        setBitsRecursive(A, left_child)
    right_child = 2*index+2
    if right_child < n and A[right_child] == 0:
        A[right_child] = 1
        setBitsRecursive(A, right_child)


def setBits(A, offset, length):
    n = len(A)
    if not A or offset < 0 or offset >= n or length <= 0:
        return 
    
    for index in range(offset, min(n, offset+length)):
        
        if A[index] == 0:
            # offset = 1
            A[index] = 1
            # Set Descendants
            setBitsRecursive(A, index)
            # Set Ancestors
            while index > 0:
                # make sure its sibling is 1, if its sibling is 0, cannot set ancestors
                if (index % 2 == 1 and index <= n-2 and A[index+1] == 1) or (index % 2 == 0 and A[index-1] == 1):
                    A[(index-1)//2] = 1  # parent
                    
                index = (index-1)//2
    return A


def clearBits(A, offset, length):
    n = len(A)
    if not A or offset < 0 or offset >= n or length <= 0:
        return 
    
    for index in range(offset, min(n, offset+length)):
        
        if A[index] == 1: 
            # offset = 0
            A[index] = 0  
            # Clear Descendants
            left_child = index
            while True:
                left_child = (left_child*2)+1
                if left_child >= n:
                    break
                A[left_child] = 0
            # Clear Ancestors
            parent = index
            while True:
                parent = (parent-1)//2
                if parent < 0 or A[parent] == 0:
                    break
                A[parent] = 0 
    return A
    

if __name__ == "__main__":
    A = [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    #print(setBits(A, 1, 3)) # offset, length, set the bits in the range from offset to offset + length - 1
    print(f"Input = {A}")
    #print(f"clBOp = {clearBits(A, 7, 3)}") # clear the bits in the range from offset to offset + length - 1
    print(f"stBOp = {setBits(A, 12, 1)}") # clear the bits in the range from offset to offset + length - 1