# LeetCode Link - https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # merge the newInterval with Intervals if any
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            #print(intervals[i])
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        result.append([newInterval[0], newInterval[1]])
        
        #merge all the intervals after the newIntervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
            
        return result

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
