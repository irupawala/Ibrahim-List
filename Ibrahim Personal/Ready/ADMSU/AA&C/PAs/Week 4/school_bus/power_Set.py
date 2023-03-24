# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:46:40 2021

@author: 1000249643
"""

import math

def printPowerSet(set):
    
    set_size = len(set)
    pow_set_size = (int) (math.pow(2, set_size)) # set_size of power set of a set with set_size n is (2**n -1)
    power_set = []
    
    for counter in range(pow_set_size):
        sub_set = []
        for binary in range(set_size):
            if ((1 << binary) & counter) > 0:
                sub_set.append(set[binary])
        power_set.append(sub_set)    
    return power_set
        
        
        
set = range(4)
print(printPowerSet(set))        