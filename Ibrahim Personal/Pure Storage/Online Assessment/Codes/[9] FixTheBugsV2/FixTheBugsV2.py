# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:01:17 2022

@author: 1000249643
"""

def countPairs(array, diff):
    pairs = 0
    n = len(array)
    i, j = 0, 1
    while i < n:
        for j in range(i, n):
            if array[j] == array[i] + diff:
                print(array[i], array[j])
                pairs += 1
        i += 1
                
    return pairs

if __name__ == "__main__":
    # print(countPairs([1, 2, 3, 4, 6, 7, 8], 2))
    # print(countPairs([1, 3, 5, 7, 9, 11, 13, 15], 2))
    print(countPairs([1, 3, 5, 7, 9, 11, 13, 15], 4))