# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:17:43 2022

@author: 1000249643
"""

def racing_results(lst):
    winner = [0, 0] # racer_name, total_points
    
    points_table = {1:10, 2:6, 3:4, 4:3, 5:2, 6:1}
    racer_points = {} # racer_name : total_points
    zero_points_racer = []
    
    for i in lst:
        race, racer_name, position = i[0], i[1], i[2]
        racer_points[racer_name] = racer_points.get(racer_name, 0) + points_table.get(position, 0)
        
        current_racer_total = racer_points[racer_name]
        winner_racer_name = winner[0]
        winner_racer_total = winner[1]
        
        if current_racer_total > winner_racer_total:
            winner = [racer_name, current_racer_total]
        elif current_racer_total == winner_racer_total:
            if racer_name < winner_racer_name:
                winner = [racer_name, current_racer_total]
                
        if racer_name in zero_points_racer and current_racer_total != 0:
            zero_points_racer.remove(racer_name)
            
        if current_racer_total == 0 and racer_name not in zero_points_racer:
            zero_points_racer.append(racer_name)
    '''            
    for key, value in racer_points.items():
        if value == 0: # racer with 0 points
            zero_points_racer.append(key)
    '''
            
    print(*(winner))
    print(*(zero_points_racer))

    
if __name__ == "__main__":
    #racing_results([[2001, 1001, 3], [2001, 1002, 2], [2002, 1003, 1], [2002, 1001, 2], [2002, 1002, 3], [2001, 1003, 1]])
    racing_results([[2001, 1001, 7], [2001, 1002, 7], [2002, 1003, 8], [2002, 1001, 8], [2002, 1002, 3], [2001, 1003, 6]])
