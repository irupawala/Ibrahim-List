# LeetCode Link - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        
        for i in range(len(intervals)):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                    
        return result
    
'''
Time Complexity - O(NlogN) + O(N)
Space Complexity - O(N)
'''
