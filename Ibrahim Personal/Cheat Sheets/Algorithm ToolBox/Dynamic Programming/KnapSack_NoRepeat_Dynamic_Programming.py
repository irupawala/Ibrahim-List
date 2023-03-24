# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:45:45 2021

@author: 1000249643
"""


def knapSackNoRepeat(total_weight):
    
    for w in range(1, total_weight+1):
        for i in range(1, no_of_bars+1):
         
             memoization_table[i][w] = memoization_table[i-1][w]
             
             wi = bars_weight[i-1]
             if wi <= w:
                 W = memoization_table[i-1][w-wi] + wi # Repetition not allowed. WE are never calculating weight considering the best acheieved in the same row thus repetition is NOT Allowed
                # W = memoization_table[i][w-wi] + wi # Repetition is allowed
                 
                 if memoization_table[i][w] < W:
                     memoization_table[i][w] = W
                                
    return memoization_table[no_of_bars][total_weight]

if __name__ == "__main__":
#    total_weight, no_of_bars = map(int, input().split())
#    bars_value = list(map(int, input().split()))
    
    total_weight, no_of_bars = 10, 3
    bars_weight = [1,4,8]    
  
    memoization_table = [[0 for x in range(total_weight+1)] for y in range(no_of_bars+1)]
    print(knapSackNoRepeat(total_weight))
    
'''

Time Complexity - O(n2^log W) [pseudo-polynomial]

Space Complexity - O(total_weight*no_of_bars)

'''