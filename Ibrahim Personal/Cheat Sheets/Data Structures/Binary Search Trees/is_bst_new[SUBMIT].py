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
        self.result = []
        self.root_index = 0

    def read (self):
        for i in range(self.nodes):
            elements = list(map(int, input().split()))
#            elements = list(map(int, sys.stdin.readline().strip().split()))            
            self.key[i] = elements[0]
            self.left_index[i] = elements[1]
            self.right_index[i] = elements[2]

    def InOrderTraversal(self, key_index):
        if key_index == -1: 
            return
        self.InOrderTraversal(self.left_index[key_index])
        self.result.append(self.key[key_index])
        self.InOrderTraversal(self.right_index[key_index])

    def IsBinarySearchTree(self):
      # Implement correct algorithm here  
      self.InOrderTraversal(self.root_index)
      
      # return false if previous element is greater then current
      for i in range(1, len(self.result)):
          if self.result[i-1] >= self.result[i]:
              return False
      return True


#if __name__ == "__main__":
def main():
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

threading.Thread(target=main).start()
            
  