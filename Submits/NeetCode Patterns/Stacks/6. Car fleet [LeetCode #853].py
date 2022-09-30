# LeetCode Link - https://leetcode.com/problems/car-fleet/

from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        
        stack  = deque()
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s) # appending the time at which the car will reach destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # Comparing the top of the stack with the element element below it, if it is smaller then the one below it means that collision will happen. At the end, the stack will contain the number of car fleets that is non-colliding cars
                stack.pop()
            
        return len(stack)
    
'''
Time Complexity - O(nlogn) + O(n)
Space Complexity - O(n) for stack
'''
