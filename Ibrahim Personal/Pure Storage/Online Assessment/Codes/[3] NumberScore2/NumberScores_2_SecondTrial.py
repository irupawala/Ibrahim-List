# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:06:36 2022

@author: 1000249643
"""

def scoring(number):
    str_number = str(number)
    list_number = [int(x) for x in str_number]
    total_points = 0
    
    # points for 7
    seven_points = list_number.count(7)
    total_points += seven_points
    
    # points for 3 multiple
    if number % 3 == 0:
        total_points += 2
        
    # points for even number
    for no in list_number:
        if no % 2 == 0:
            total_points += 4
              
    # points for consecutive numbers
    j = 0
    while j < len(list_number):
        sequence_length = 0
        while j < len(list_number)-1 and list_number[j+1] == list_number[j]-1:
            sequence_length += 1
            j += 1

        total_points += (sequence_length+1)**2
        
        j += 1            

    # points for consecutive fives
    i = 0
    while i < len(list_number):
        five_counts = 0
        while i < len(list_number)-1 and list_number[i] == 5 and list_number[i+1] == 5:
            five_counts += 1
            i += 1 
        if five_counts > 0:
            total_points += ((five_counts)*3) # for pairs
            if five_counts+1 > 2:
                total_points += ((five_counts+1-2)*3)
        
        i += 1

    return total_points


number = 8555356638
print(scoring(number))