# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:14:16 2022

@author: 1000249643
"""

def calculate_n(A):
    levels  = len(A)
    n = 0
    for i in range(levels):
        n += 2**i
    return n

def find (A, offset):
    for x in range(len(A)):
        for y in range(len(A[x])):
            if offset == 0:
                return x, y
            offset -= 1
    return 


def setBitsRecursive_2D(A, child_i, child_j):
    if child_i >= len(A)-1 or child_j >= len(A[child_i]): return 
    # Set left child
    left_child_i = child_i + 1
    left_child_j = 2 * child_j
    
    if (left_child_i < len(A)-1 or left_child_j < len(A[left_child_i])) and A[left_child_i][left_child_j] == 0:
        A[left_child_i][left_child_j] = 1
        setBitsRecursive_2D(A, left_child_i, left_child_j)
        
    # Set right child
    right_child_i = child_i + 1
    right_child_j = (2*child_j) + 1
    if (right_child_i < len(A)-1 or right_child_j < len(A[right_child_i])) and A[right_child_i][right_child_j] == 0:
        A[right_child_i][right_child_j] = 1
        setBitsRecursive_2D(A, right_child_i, right_child_j)
    


def setBits_2D(A, offset, length):
    n = calculate_n(A) 
    if not A or offset < 0 or offset >= n or length <= 0:
        return 
    
    offset_x, offset_y = (find(A, offset))   
    length_offset = -1
    for i in range(offset_x, len(A)):
        for j in range(offset_y, len(A[offset_x])):
            # length reached
            length_offset += 1
            if length_offset == length:
                return A
            
            if A[i][j] == 0:
                A[i][j] = 1
                
                # Set Descendants
                child_i, child_j = i, j
                setBitsRecursive_2D(A, child_i, child_j)
                
                # Set Ancestors
                parent_i, parent_j = i, j
                while True:
                    if parent_i < 0 or parent_j < 0:
                        break
                    # make sure its sibling is 1, if its sibling is 0, cannot set ancestors
                    if (parent_j % 2 == 1 and A[parent_i][parent_j-1] == 1) or (parent_j % 2 == 0 and A[parent_i][parent_j-1] == 1):
                        A[parent_i-1][parent_j // 2] = 1 # parent
                            
                    parent_i = parent_i-1
                    parent_j = parent_j // 2
    return 
                

def clearBits_2D(A, offset, length):
    n = calculate_n(A)
    if not A or offset < 0 or offset >= n or length <= 0:
        return 
    
    offset_x, offset_y = (find(A, offset))
    length_offset = -1
    for i in range(offset_x, len(A)):
        for j in range(offset_y, len(A[offset_x])):
            # length reached
            length_offset += 1
            if length_offset == length:
                return A
            
            #print(i, j)
            if A[i][j] == 1:
                A[i][j] = 0
            
                # Clear Descendants
                child_i, child_j = i, j
                while True:
                    child_i = child_i+1
                    child_j = (2*child_j)
                    #print(child_i, child_j)
                    if child_i >= len(A)-1 or child_j >= len(A[child_i]):
                        break
                    A[child_i][child_j] = 0
                
                # Clear Ancestors
                parent_i, parent_j = i, j
                while True:
                    parent_i = parent_i-1
                    parent_j = (parent_j)//2
                    if parent_i < 0 or parent_j < 0 or A[parent_i][parent_j] == 0:
                        break
                    A[parent_i][parent_j] = 0
                
                
    return
                

if __name__ == "__main__":
    A = [[0], [0, 0], [1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1]]
    print(f"Input = {A}")
    #print(f"clBOp = {clearBits_2D(A, 7, 3)}") # clear the bits in the range from offset to offset + length - 1
    print(f"stBOp = {setBits_2D(A, 12, 1)}") # clear the bits in the range from offset to offset + length - 1