# python3

import sys
import threading

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(2100000000)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()

'''
Running time - O(n * len(branch))
'''


'''
Calculates the height of each node and then returns the maximum of the heights
'''

def calculate_height(parent): 
    
    if (tree[parent] == []):
        Max_height = 1
        tree_height[parent] = Max_height
        return (Max_height)    
        
    
    Max_height = 1
    for child in tree[parent]:
        
        if tree_height[child] != 0:
            next = tree_height[child]
        else:
            next = calculate_height(child)        


        if (Max_height < next + 1):            
            Max_height = next + 1
            tree_height[child] = Max_height
            

    return(Max_height)    


def compute_height(n, parents):
    
    global tree 
    global tree_height
    
    tree = [ [] for _ in range(n)]
    tree_height = [ 0 for _ in range(n)]
    
    for child, parent in enumerate(parents):
        if(parent == -1):
            root = child
        else:
            tree[parent].append(child)
#    
#    print (f"root = {root}")
#    for index, node in enumerate(tree):
#        print (f"{index} : {node}")
#    
#    
    

    for parent, child in enumerate(tree): 
        
        if(tree_height[parent] == 0):
            Max_height = calculate_height(parent);                  
            tree_height[parent] = Max_height   
 
            
    return max(tree_height)


def main():
#    n = int(input("Enter the number of nodes = "))
#    parents = list(map(int, input("Enter the value of nodes = ").split()))
    n = int(input())
    parents = list(map(int, input().split()))    
    print(compute_height(n, parents))



############################################# Unit Testing ###############################################
    
import os     
def test():
    

    filename_list = []
    for root, dirs, files in os.walk("./tests"):
#    for root, dirs, files in os.walk("./test_case"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
            
        f=open("./tests/" + filename, "r")
#        f=open("./test_case/" + filename, "r")        
        if f.mode == 'r':
            
            
            ###############################################################
            test_input = f.read().rstrip('\n')
            f.close()
            lines =  test_input.splitlines()
            n = int(lines[0])
            parents = list(map(int, lines[1].split()))   
            ###############################################################

        f=open("./tests/" + filename + '.a', "r")
#        f=open("./test_case/" + filename + '.a', "r")        
        if f.mode == 'r':
            expected_output =f.read().rstrip('\n')
            f.close()
            
        output = compute_height(n, parents)
        
 
#        print('Input: ' + str(test_input))
        print('Expected Output: ' + str(expected_output))
        print('Ouput: ' + str(output))



        if str(expected_output)==str(output):
            print('Test Passed')
        else:
            print('Test Failed')
            break    

#    print("Passed all tests !!")
       
       

#############################################################################################################
            
##################################################### Failed Case ###########################################
            
def failed_test():
    

    filename_list = []
#    for root, dirs, files in os.walk("./tests"):
    for root, dirs, files in os.walk("./test_case"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
            
#        f=open("./tests/" + filename, "r")
        f=open("./test_case/" + filename, "r")        
        if f.mode == 'r':
            
            
            ###############################################################
            test_input = f.read().rstrip('\n')
            f.close()
            lines =  test_input.splitlines()
            n = int(lines[0])
            parents = list(map(int, lines[1].split()))   
            ###############################################################

#        f=open("./tests/" + filename + '.a', "r")
        f=open("./test_case/" + filename + '.a', "r")        
        if f.mode == 'r':
            expected_output =f.read().rstrip('\n')
            f.close()
            
        output = compute_height(n, parents)
        
 
        print('Input: ' + str(test_input))
        print('Expected Output: ' + str(expected_output))
        print('Ouput: ' + str(output))



        if str(expected_output)==str(output):
            print('Test Passed')
        else:
            print('Test Failed')
            break      
        

#######################################################################################################


threading.Thread(target=main).start()
#threading.Thread(target=test).start()

#
#if __name__ == "__main__":
##    main()
##    test()
#    
##    failed_test()
    
    
    
''' 

5 -1 0 4 0 3
5 4 -1 4 1 1 
100 96 61 95 34 12 26 48 42 69 74 90 67 8 53 65 0 14 47 88 8 49 4 93 75 6 29 -1 62 87 12 42 52 1 46 4 83 14 75 72 95 15 86 29 53 85 78 65 31 5 96 6 74 87 24 15 90 22 85 20 46 78 97 50 97 69 19 21 61 92 5 22 47 63 1 93 28 20 34 52 21 72 88 67 0 86 49 63 48 28 25 50 83 31 19 62 24 64 64 92 25

'''


