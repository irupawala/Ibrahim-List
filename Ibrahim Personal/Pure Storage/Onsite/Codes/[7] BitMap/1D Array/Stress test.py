def setbit_down(A, x, n):
    if x>=n:
        return
    if 2*x+1<=n and A[2*x+1]==0:
        A[2*x+1]=1
        setbit_down(A,2*x+1,n)
    if 2*x+2<=n and A[2*x+2]==0:
        A[2*x+2]=1
        setbit_down(A,2*x+2,n)
    

def set_bit(A, pos, length):
    if not A or pos<0 or length<=0:
        return
    n = len(A)-1    #last index of A
    for x in range(pos, min(n+1,min(pos+length, 2*pos+1))):
        # set self
        if A[x] == 1:
            continue
        A[x]=1
        # set descendants
        setbit_down(A,x,n)
        # set ancestors
        while x>0:
            # make sure its sibling is 1, if its sibling is 0, cannot set ancestors
            if (x%2==0 and A[x-1]==1) or (x%2==1 and x<n and A[x+1]==1):
                A[int((x-1)/2)] = 1
            x = int((x-1)/2)
            
    return A

def clear_bit(A, pos, length):
    if not A or pos<0 or length<=0:
        return
    n = len(A)-1    #last index of A
    for x in range(pos, min(n+1, pos+length)):
        # clear self
        if A[x]==0:
            continue
        A[x]=0
        # clear descendants
        while 2*x+1<=n:
            A[2*x+1] = 0
            x=2*x+1
        # clear ancestors
        while x>0:
            if A[int((x-1)/2)]==0:
                break
            A[int((x-1)/2)] = 0
            x = (x-1)/2
    return A
        
####################################################################################################################

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

####################################################################################################################

if __name__ == "__main__":

    while True:
        
        import random
        randomlist = []
        for i in range(15):
            n = random.randint(0,1)
            randomlist.append(n)
        #print(randomlist)
        
        offset = random.randint(0, len(randomlist)-1)
        length = random.randint(0, (len(randomlist)-1)//2)        
            
            
        if set_bit(randomlist, offset, length) != setBits(randomlist, offset, length):
            print(f"Error in set_bit A = {randomlist}, offset = {offset}, length = {length}")
            print(f"SolSB = {set_bit(randomlist, offset, length)}") # clear the bits in the range from offset to offset + length - 1    
            print(f"stBOp = {setBits(randomlist, offset, length)}") # clear the bits in the range from offset to offset + length - 1
            break
        if clear_bit(randomlist, offset, length) != clearBits(randomlist, offset, length):
            print(f"Error in clear_bit A = {randomlist}, offset = {offset}, length = {length}")
            print(f"SolCB = {clear_bit(randomlist, offset, length)}") # clear the bits in the range from offset to offset + length - 1
            print(f"clBOp = {clearBits(randomlist, offset, length)}") # clear the bits in the range from offset to offset + length - 1
            break
        print(f"OKAY for A = {randomlist}")