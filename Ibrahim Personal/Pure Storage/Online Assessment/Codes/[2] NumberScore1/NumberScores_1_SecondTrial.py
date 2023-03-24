# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:06:36 2022

@author: 1000249643
"""

def scoring(number):
    str_number = str(number)
    list_number = [int(x) for x in str_number]
    total_points = 0
    
    # points for 9
    nine_points = list_number.count(9)
    total_points += (nine_points*4)
    
    # points for 7 multiple
    if number % 7 == 0:
        total_points += 1
        
    # points for even number
    for no in list_number:
        if no % 2 == 0:
            total_points += 2
              
    # points for consecutive numbers
    j = 0
    while j < len(list_number):
        sequence_length = 0
        while j < len(list_number)-1 and list_number[j+1] == list_number[j]+1:
            sequence_length += 1
            j += 1

        total_points += (sequence_length+1)**2
        
        j += 1            

    # points for consecutive ones
    i = 0
    while i < len(list_number):
        one_counts = 0
        while i < len(list_number)-1 and list_number[i] == 1 and list_number[i+1] == 1:
            one_counts += 1
            i += 1 
        if one_counts > 0:
            total_points += ((one_counts)*5) # for pairs
            if one_counts+1 > 2:
                total_points += ((one_counts+1-2)*5)
        
        i += 1

    return total_points


number = 0 
print(scoring(number))