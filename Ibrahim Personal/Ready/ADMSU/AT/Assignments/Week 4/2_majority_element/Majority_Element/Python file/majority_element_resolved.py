# Uses python3

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:03:08 2020

@author: 1000249643
"""

# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    print(f'left = {left}')
    print(f'right = {right}')    

    middle = (left + right) // 2
    half_elements_count = (right - left) // 2
    
    print(f'middle = {middle}')
    print(f'half_elements_count = {half_elements_count}')
    print(f'a = {a}')

    left_majority = get_majority_element(a, left, middle)
    right_majority = get_majority_element(a, middle, right)
    
    
    print(f'left = {left}')
    print(f'right = {right}')        
    print(f'left_majority = {left_majority}')
    print(f'right_majority = {right_majority}')

    left_majority_count = get_number_of_element_count(a, left, right, left_majority)
    
    print(f'left_majority_count = {left_majority_count}') 
    if left_majority_count > half_elements_count:
        return left_majority

    right_majority_count = get_number_of_element_count(a, left, right, right_majority)
    
    print(f'right_majority_count = {right_majority_count}') 
    if right_majority_count > half_elements_count:
        return right_majority

    return -1

def get_number_of_element_count(a, left, right, x):
    maj_count = 0
    for i in range(left, right):
        if a[i] == x:
            maj_count += 1
    return maj_count

if __name__ == '__main__':
    
    '''
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    '''
    
    # number of elements 
    n = int(input("Enter number of elements : ")) 

    # Below line read inputs from user using map() function 
    #n, *a = list(map(int, input("\nEnter the numbers : ").split()))
    a = list(map(int, input("\nEnter the numbers : ").split()))
    
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


