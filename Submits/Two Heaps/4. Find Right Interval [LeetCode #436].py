from heapq import *

class Solution:
    def findRightInterval(self, intervals):
        start, end = 0, 1
        
        maxStartHeap, maxEndHeap = [], []
        result = [0 for i in range(len(intervals))]
        
        for i in range(len(intervals)):
            heappush(maxStartHeap, (-intervals[i][start], i))
            heappush(maxEndHeap, (-intervals[i][end], i))
            
        for _ in range(len(intervals)):
            topEnd, endIndex = heappop(maxEndHeap)
            result[endIndex] = -1 # defaults to -1
            if -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)            
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                result[endIndex] = startIndex
                heappush(maxStartHeap, (topStart, startIndex))
        
        return result
 
'''
S = Solution()
print(S.findRightInterval([[3,4], [1,5], [4,6]]))
'''

'''
Time Complexity - O(N.logN)
Space Complexity - O(N)
'''
