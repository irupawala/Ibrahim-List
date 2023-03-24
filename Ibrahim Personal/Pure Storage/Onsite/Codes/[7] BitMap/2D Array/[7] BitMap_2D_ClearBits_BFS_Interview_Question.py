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



# It is assumed that the clearBits always starts from the last level hence clearing descendants is only required

# Clear Ancestors BFS Approach
def clearBits_2D_BFS(bits, start, length):
    x, y = start
    y_start, y_end = y, y + length
    while x >= 0:
        clearFlag = False
        for y in range(y_start, y_end):
            if bits[x][y] == 1:
                clearFlag = True
                bits[x][y] = 0
                
        if not clearFlag: return bits
        x, y_start, y_end = x-1, y_start//2, y_end//2
        
    return bits

# Clear Ancestors DFS Approach
def clearBits_2D_DFS(bits, start, length):
    start_x, start_y = start
    for j in range(start_y, start_y + length):
        
        #Clear Ancestors
        parent_i, parent_j = start_x, j
        while True:
            # break the loop if the bit is already cleared or root is reached
            if parent_i < 0 or bits[parent_i][parent_j] == 0:
                break
            bits[parent_i][parent_j] = 0 # clear bit
            parent_i = parent_i - 1
            parent_j = parent_j // 2
                
    return bits
        
if __name__ == "__main__":
    bits = [[0], [1, 0], [1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1]]
    # print(clearBits_2D(bits, (3,4), 4))
    print(clearBits_2D_BFS(bits, (1,0), 1))
    print(clearBits_2D_DFS(bits, (1,0), 1))