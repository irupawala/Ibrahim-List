https://leetcode.com/problems/valid-square/

import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(x, y):
            return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
        
        lengths = [distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        set_length = list(set(lengths))
        
        # For Rhombus total_length will be 3 as it does not have equal diagonals like square
        if len(set_length) != 2: return False 
        return set_length[0] > 0 and set_length[1] > 0 
    
'''
Time Complexity - O(1)
Space Complexity - O(1) 
'''