# python3


'''
All operations of heap works in time O(logn).
Now as there are n/2 elements to be shiftdown. Running time = (n/2)log(n/2) ~ nlogn
'''







import os
import sys
import threading

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(2100000000)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()


class build_heap(): # Creating a heap so that list is not required to pass from one function to another 
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.swaps = []
        
    def siftdown(self, i):
        leftChild = (2*i) + 1
        rightChild = (2*i) + 2
        
        minIndex = i
        
        l = leftChild 
        if l < self.size and self.data[l] < self.data[minIndex]:
            minIndex = l
            
        r = rightChild 
        if r < self.size and self.data[r] < self.data[minIndex]:
            minIndex = r
            
        if i != minIndex: # If minIndex and i are equal it means that the node has no childrens
            self.swaps.append((i, minIndex))
            self.data[i], self.data[minIndex] = self.data[minIndex], self.data[i]
            self.siftdown(minIndex)

    
    def build_swaps(self):

        for i in reversed (range (len(self.data)//2  + 1)):
            self.siftdown(i)

        return self.swaps
            

'''
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
#    swaps = []
#    for i in range(len(data)):
#        for j in range(i + 1, len(data)):
#            if data[i] > data[j]:
#                swaps.append((i, j))
#                data[i], data[j] = data[j], data[i]
#    return swaps
    
    swaps = []
    for i in reversed(range(len(data)//2)):
        swaps.append(SiftDown(i))
        
    return swaps
'''


##################################################### Main Function ###########################################


def main():
    n = int(input())
    data_input = list(map(int, input().split()))
    assert len(data_input) == n
    
#    data_input = [6, 7, 1, 0, 9, 3]
    
    data_class_instance = build_heap(data = data_input)
    swaps = data_class_instance.build_swaps()


    print(len(swaps))
    for i, j in swaps:
        print(i, j)



#############################################################################################################
            
##################################################### Failed Case ###########################################
            
def failed_test():
    

    filename_list = []
#    for root, dirs, files in os.walk("./tests"):
    for root, dirs, files in os.walk("./tests"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
            
#        f=open("./tests/" + filename, "r")
        f=open("./tests/" + filename, "r")        
        if f.mode == 'r':
            
            
            ###############################################################
            test_input = f.read().rstrip('\n')
            f.close()
            lines =  test_input.splitlines()
            n = int(lines[0])
            data_input = list(map(int, lines[1].split()))   
            ###############################################################

#        f=open("./tests/" + filename + '.a', "r")
        f=open("./tests/" + filename + '.a', "r")        
        if f.mode == 'r':
            expected_output =f.read().rstrip('\n')
            f.close()
        
        data_class_instance = build_heap(data = data_input)
        output = data_class_instance.build_swaps()
        
 
        print('Input: ' + (test_input))
        print('Expected Output: ' + (expected_output))
#        print('Ouput: ' + str(output))
        print('-----------------------------Output----------------------------------')
        print(len(output))
        for i, j in output:
            print(i, j)



        if (expected_output)==(output):
            print('Test Passed')
        else:
            print('Test Failed')
            break      
            
############################################## Test Run  ############################################################
            
if __name__ == "__main__":
    main()

        
#threading.Thread(target=main).start()
#threading.Thread(target=failed_test).start()    