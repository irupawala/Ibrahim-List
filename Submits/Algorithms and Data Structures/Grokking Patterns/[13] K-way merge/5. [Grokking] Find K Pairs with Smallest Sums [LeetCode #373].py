# LeetCode Link - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        maxHeap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(maxHeap) < k:
                    heappush(maxHeap, (-(nums1[i]+nums2[j]), i, j) )
                else:
                    if nums1[i] + nums2[j] > -maxHeap[0][0]:
                        break
                    else:
                        heappop(maxHeap)
                        heappush(maxHeap, (-(nums1[i]+nums2[j]), i, j) )
                
        result = []
        for (num, i, j) in maxHeap:
            result.append([nums1[i], nums2[j]])

        return result
    
'''
Time Complexity - O(N.M.logK) # If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(K^2logK), because we are not iterating more than ‘K’ elements in both arrays.
Space Complexity - O(K)
'''
