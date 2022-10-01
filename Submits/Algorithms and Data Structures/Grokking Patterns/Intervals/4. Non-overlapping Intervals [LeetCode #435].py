# LeetCode Link - https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        i, start, end = 0, 0, 1
        last = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][start] < last[end]:
                count += 1   
            else:
                last = intervals[i]
        return count
        
'''
Time Complexity - O(NlogN) + O(N)
Space Complexity - O(N) for sorting 
'''
