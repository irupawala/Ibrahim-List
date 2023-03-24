# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 05:38:44 2021

@author: 1000249643
"""
def power_set(n):
    
    set_size = n
    power_set_size = (int) (2**n)
    power_set = []
    
    for counter in range(power_set_size):
        sub_set = []
        for binary in range(set_size):
            if ((1 << binary) & counter) > 0:
                sub_set.append(binary)
        power_set.append(sub_set)
        
    return power_set



n = 3
print(power_set(3))