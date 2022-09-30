LeetCode Link - https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import *
import math

class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for p in points:
            heappush(minHeap, (math.sqrt(p[0]**2 + p[1]**2), p))
            
        output = []
        for _ in range(k):
            output.append(heappop(minHeap)[1])
            
        return output
        
'''
Time Complexity - O(nlogn)
Space Complexity - O(n) for heap
'''
