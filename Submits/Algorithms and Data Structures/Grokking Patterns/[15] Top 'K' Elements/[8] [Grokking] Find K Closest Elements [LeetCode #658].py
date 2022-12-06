# Leetcode Link - https://leetcode.com/problems/find-k-closest-elements/

from heapq import *

class Solution:
    def findClosestElements(self, arr, k, x):
        index = self.binary_search(arr, x)
        low, high = index - k, index + k

        low = max(low, 0)  # 'low' should not be less than zero
        # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)

        minHeap = []
        # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))

        # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(k):
            result.append(heappop(minHeap)[1])

        result.sort()
        return result        
    
    def binary_search(self, arr,  target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > 0:
            return low - 1
        return low    
    
'''
Time Complexity - O(logN+K∗logK)
Space Complexity - O(K∗logK)
'''
