# Using minHeap
from heapq import *
import math

'''
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

'''
Time Complexity - O(nlogn)
Space Complexity - O(n) for heap
'''

# Using maxHeap
class Solution:
    def kClosest(self, points, k):
        maxHeap = []
        
        for p in points:
            if k > 0:
                heappush(maxHeap, (-math.sqrt(p[0]**2 + p[1]**2), p))
                k -= 1 
            
            else:
                dist = -math.sqrt(p[0]**2 + p[1]**2)
                if dist > maxHeap[0][0]:
                    heappop(maxHeap)
                    heappush(maxHeap, (dist, p))
                        
        output = []
        while maxHeap:
            output.append(heappop(maxHeap)[1])
            
        return output
        
'''
Time Complexity - O(NlogK)
Space Complexity - O(K) for heap
'''
