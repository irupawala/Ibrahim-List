# LeetCode Link - https://leetcode.com/problems/last-stone-weight/

from heapq import *

class Solution:
    def lastStoneWeight(self, stones) :
        maxHeap = []
        for s in stones: 
            heappush(maxHeap, -s)
        
        while len(maxHeap) > 1:
            stone1 = heappop(maxHeap)
            stone2 = heappop(maxHeap)
            
            if stone1 == stone2:
                heappush(maxHeap, 0)
            else:
                heappush(maxHeap, -abs(stone1-stone2))
                
        return -maxHeap[0]
        
'''
Time Complexity - O(nlogn)
Space Complexity - O(n) for heap
'''
