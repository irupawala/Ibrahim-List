# python3
#!/usr/bin/python3
import sys, threading
import math

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders():
    def __init__(self, nodes):
        self.nodes = nodes
        self.key = [-1] * self.nodes
        self.left_index = [-1] * self.nodes
        self.right_index = [-1] * self.nodes

    def read (self): #reading binary trees into key, left, right
        for i in range(self.nodes):
#            elements = list(map(int, input().split()))
            elements = list(map(int, sys.stdin.readline().strip().split()))            
            self.key[i] = elements[0]
            self.left_index[i] = elements[1]
            self.right_index[i] = elements[2]
            
    def IsBinarySearchTree(self):

        def PreOrderTraversalLeft(node_index, min_limit, max_limit, flag_right_traversal):
            if node_index == -1:
                return True
            if (flag_right_traversal): # If flag True then it means that right traversal has happened somewhere before hence >=
                if ((self.key[node_index] >= min_limit) and (self.key[node_index] < max_limit)):
                    result = PreOrderTraversalLeft(self.left_index[node_index], min_limit, self.key[node_index], flag_right_traversal)
                    if (result == False):
                        return False 
                    result = PreOrderTraversalRight(self.right_index[node_index], self.key[node_index], max_limit, flag_right_traversal)
                    if (result == False):
                        return False          
                else:
                    return False
                return True   
            else: # else if there was no right traversal then checking only >
                if ((self.key[node_index] > min_limit) and (self.key[node_index] < max_limit)):
                    result = PreOrderTraversalLeft(self.left_index[node_index], min_limit, self.key[node_index], flag_right_traversal)
                    if (result == False):
                        return False                 
                    result = PreOrderTraversalRight(self.right_index[node_index], self.key[node_index], max_limit, flag_right_traversal)
                    if (result == False):
                        return False          
                else:
                    return False
                return True         
        
        
        def PreOrderTraversalRight(node_index, min_limit, max_limit, flag_right_traversal): 
            flag_right_traversal = 1 # using flag for corner cases when there is same node in the left leaf of right subtree example 4, [10 -1 1], [20, 2, -1], [15, 3, -1], [10, -1, -1]
            if node_index == -1:
                return True
            if ((self.key[node_index] >= min_limit) and (self.key[node_index] < max_limit)): # >= as the node on the right subtree can be same also
                result = PreOrderTraversalLeft(self.left_index[node_index], min_limit, self.key[node_index], flag_right_traversal)
                if (result == False): #if false is returned no need to check any further just return false
                    return False  
                result = PreOrderTraversalRight(self.right_index[node_index], self.key[node_index], max_limit, flag_right_traversal)
                if (result == False):
                    return False          
            else:
                return False
            return True                
        
        
        def PreOrderTraversal(node_index, min_limit, max_limit):
            if (PreOrderTraversalLeft(self.left_index[node_index], min_limit, self.key[node_index], 0) == False):
                return False
            return(PreOrderTraversalRight(self.right_index[node_index], self.key[node_index], max_limit, 0))
            
        return (PreOrderTraversal(0, -math.inf, math.inf))      
      


def main():
    nodes = int(sys.stdin.readline().strip())
#    nodes = int(input().strip())
    if nodes == 0:
        print("CORRECT")
    else:
        Tree = TreeOrders(nodes)
        Tree.read()
        if Tree.IsBinarySearchTree():      
            print("CORRECT")
        else:
            print("INCORRECT")

#    input("press close to exit") 

threading.Thread(target=main).start()
           
  