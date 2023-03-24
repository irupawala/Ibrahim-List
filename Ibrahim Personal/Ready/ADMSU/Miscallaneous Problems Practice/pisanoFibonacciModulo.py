# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 10:18:12 2022

@author: 1000249643
"""

def pisanoPeriod(m):
    previous, current = 0, 1
    pisanoSequence = [0, 1]
    
    for i in range(m*m): # Pisano period ranges from 3 to m*m
       previous, current = current, (previous + current) % m
       pisanoSequence.append(current)
       
       if previous == 0 and current == 1:
           return pisanoSequence[:-2], len(pisanoSequence)-2
    

def pisanoFibonacci(n, m):
    
    pisano_sequence, pisano_period = pisanoPeriod(m)
    
    # Taking mod of N with pisano_period    
    n = n % pisano_period
    return pisano_sequence[n]
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(pisanoFibonacci(n, m))
    
'''
For more details visit https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/
Time Complexity - O(n^2)
Space Complexity - O(n^2)
'''

