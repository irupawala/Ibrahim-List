# LeetCode Link - https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import *

class Solution:
    def findKthLargest(self, nums, k) :
        minHeap = []
        
        for no in nums:
            if len(minHeap) < k:
                heappush(minHeap, no)
            elif no > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, no)
                
        return minHeap[0]
    
'''
Time Complexity - O(nlogn)
Space Complexity - O(n)
'''
