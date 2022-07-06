# LintCode Link - https://www.lintcode.com/problem/919/

# NeetCode Solution 

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start_time, end_time = [], []
        for i in range(len(intervals)):
            start_time.append(intervals[i].start)
            end_time.append(intervals[i].end)

        start_time.sort()
        end_time.sort()
        meeting_count, result, start, end = 0, 0, 0, 0

        for start in range(len(start_time)):
            meeting_count += 1
            if start_time[start] >= end_time[end]:
                meeting_count -= 1
                end += 1
            result = max(result, meeting_count)
        return result

'''
Time Complexity - O(nlogn) for sorting
Space Complexity - O(n)
'''

# Grokking Solution 

