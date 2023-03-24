# python3
#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


'''

To solve this problem, see that at any node it's key is lesser then max limit and greater then max limit
min limit and max limit is the parent node and it is adjusted based on in which direction tree is traversing

Running Time  - O(Height)

'''


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  print(tree)
  return True

class TreeOrders():
    def __init__(self, nodes):
        self.nodes = nodes
        self.key = [-1] * self.nodes
        self.left_index = [-1] * self.nodes
        self.right_index = [-1] * self.nodes

    def read (self):
        for i in range(self.nodes):
            elements = list(map(int, input().split()))
#            elements = list(map(int, sys.stdin.readline().strip().split()))            
            self.key[i] = elements[0]
            self.left_index[i] = elements[1]
            self.right_index[i] = elements[2]
            
    def IsBinarySearchTree(self):
      # Implement correct algorithm here  
      
        def PreOrderTraversal(node_index, min_limit, max_limit):
            if node_index == -1:
                return True
            if ((self.key[node_index] > min_limit) and (self.key[node_index] < max_limit)):
                result = PreOrderTraversal(self.left_index[node_index], min_limit, self.key[node_index])
                if (result == False):
                    return False
                result = PreOrderTraversal(self.right_index[node_index], self.key[node_index], max_limit)
                if (result == False):
                    return False                
            else:
                return False
            return True
            
        return (PreOrderTraversal(0, -math.inf, math.inf))      
      
'''
if __name__ == "__main__":
#    nodes = int(sys.stdin.readline().strip())
    nodes = int(input().strip())
    if nodes == 0:
        print("CORRECT")
    else:
        Tree = TreeOrders(nodes)
        Tree.read()
        if Tree.IsBinarySearchTree():      
            print("CORRECT")
        else:
            print("INCORRECT")

    input("press close to exit") 
'''    


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
            
  