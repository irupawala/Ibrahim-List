# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:51:00 2022

@author: 1000249643
"""

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


'''
To Solve this do pre-order traversal first then return false if previous element is greater then current
Running time is O(n) [InOrderTraversal] + O(n)[Checking values] ~= O(n)
'''


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
        return 


    def IsBinarySearchTree(self):
      # Implement correct algorithm here  
      stack = []
      stack.append((float('-inf'), 0, float('inf')))

      while stack:
          min, node_index, max = stack.pop()
          node_key = self.key[node_index]

          if node_key < min or node_key >= max:
              return False
          
          if self.left_index[node_index] != -1:
              stack.append((min, self.left_index[node_index], node_key))
              
          if self.right_index[node_index] != -1:
              stack.append((node_key , self.right_index[node_index], max))

      return True
              

if __name__ == "__main__":
#def main():
#    nodes = int(sys.stdin.readline().strip())
    nodes = int(input().strip())
    
    Tree = TreeOrders(nodes)
    Tree.read()
    if nodes == 0 or Tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")

#threading.Thread(target=main).start()
            
  