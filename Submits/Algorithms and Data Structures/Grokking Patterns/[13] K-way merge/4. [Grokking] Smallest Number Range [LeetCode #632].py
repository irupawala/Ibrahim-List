# LeetCode Link - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from heapq import *

class Solution:
    def smallestRange(self, nums):
        minHeap = []
        rangeStart, rangeEnd = 0, float("inf")
        currentMaxNumber = float("-inf")

        # put the 1st element of each array in the max heap
        for arr in nums:
            heappush(minHeap, (arr[0], 0, arr))
            currentMaxNumber = max(currentMaxNumber, arr[0])

        # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
        # if the array of the top element has more elements, insert the next element in the heap
        while len(minHeap) == len(nums):
            num, i, arr = heappop(minHeap)
            if rangeEnd - rangeStart > currentMaxNumber - num:
                rangeStart = num
                rangeEnd = currentMaxNumber

            if len(arr) > i+1:
                # insert the next element in the heap
                heappush(minHeap, (arr[i+1], i+1, arr))
                currentMaxNumber = max(currentMaxNumber, arr[i+1])

        return [rangeStart, rangeEnd]
    
    
'''
Time Complexity - O(N.logM)
Space Complexity - O(M)
'''
