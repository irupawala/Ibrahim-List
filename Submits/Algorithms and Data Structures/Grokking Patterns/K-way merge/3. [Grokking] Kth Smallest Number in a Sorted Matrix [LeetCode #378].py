# LeetCode Link - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from heapq import *

class Solution:
    def kthSmallest(self, matrix, k):
        minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap    
        for i in range(min(len(matrix), k)):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
            
    # take the smallest(top) element from the min heap, if the running ccount is equal to k return the number 
    # if the row of the top element has more elements, add the next element to the heap
    
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i+1:
                heappush(minHeap, (row[i+1], i+1, row))

        return number
        
'''
Time Complexity - O(min(K,N) + K.logN)
Space Complexity - O(N)
'''
