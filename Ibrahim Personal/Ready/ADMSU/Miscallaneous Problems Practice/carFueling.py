# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:35:50 2022

@author: 1000249643
"""


def noOfRefills(distance, capacity, stops):
    
    refill_no = 0
    tank_fuel = capacity
    
    for i in range(len(stops)-1):
        s = stops[i]
        tank_fuel -= s        
        dist = stops[i+1]-stops[i]
        
        if dist > tank_fuel:
            tank_fuel = capacity
            refill_no += 1
            
        if dist > capacity:
            return -1
            
    if distance - stops[i] > tank_fuel:
        refill_no += 1
        return refill_no
    else:
        return refill_no
        


if __name__ == "__main__":
    distance = int(input())
    capacity = int(input())
    stops_count = int(input())
    stops = list(map(int, input().split()))
    
    refills = noOfRefills(distance, capacity, stops)
    print(refills)
    