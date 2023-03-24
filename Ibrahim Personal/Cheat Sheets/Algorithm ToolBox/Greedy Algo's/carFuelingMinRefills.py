# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:35:50 2022

@author: 1000249643
"""

import sys

def compute_min_refills(distance, capacity, stops):
    
    refill_no = 0
    tank_fuel = capacity
    stops.append(distance)
    stops.insert(0,0)
    
    for i in range(1, len(stops)-1):
        dist_travelled = stops[i] - stops[i-1] 
        tank_fuel -= dist_travelled        
        dist_next = stops[i+1]-stops[i]
        
        if dist_next > tank_fuel:
            tank_fuel = capacity
            refill_no += 1
            
        if dist_next > capacity:
            return -1
            
    if distance - stops[i] > tank_fuel:
        refill_no += 1
        return refill_no
    else:
        return refill_no
        


#if __name__ == "__main__":
#     distance = int(input())
#     capacity = int(input())
#     stops_count = int(input())
#     stops = list(map(int, input().split()))
#    
#     refills = compute_min_refills(distance, capacity, stops)
#     print(refills)
 

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
 
    
"""

Time Complexity - O(n)

"""    