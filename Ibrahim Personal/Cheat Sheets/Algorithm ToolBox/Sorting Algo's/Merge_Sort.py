# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:50:27 2021

@author: 1000249643
"""

def merge(B, C):
    merged_list = []
    
    for i in range(len(B + C)):
        
        if len(B) == 0 or len(C) == 0:
            merged_list = merged_list + B + C
            return merged_list
        
        b = B[0]
        c = C[0]
        
        if b <= c:
            merged_list.append(b)
            B.remove(b)
        else:
            merged_list.append(c)
            C.remove(c)
            
    return merged_list
    

def mergeSort(input_array):
    if len(input_array) == 1:
        return input_array
    
    B = mergeSort(input_array[0 : len(input_array)//2])
    C = mergeSort(input_array[len(input_array)//2 : ])
    Aprime = merge(B, C)
    return Aprime


if __name__ == "__main__":
#    input_array = list(map(int, input().split()))
    input_array = [7, 2, 5, 3, 7, 13, 1, 6]
#    input_array = [2, 8, 3, 6, 9, 9, 9, 9, 5, 4, 1, 0, 2, 2, 9, 8, 8, 7, 7, 6, 5, 4, 3, 2, 1]
    print(mergeSort(input_array))
    
'''

Time Complexity - Minimum running time Alpha(nlogn)
    
'''