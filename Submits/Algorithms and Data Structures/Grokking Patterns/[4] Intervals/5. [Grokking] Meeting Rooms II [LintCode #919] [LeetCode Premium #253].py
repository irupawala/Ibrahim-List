# LintCode Link - https://www.lintcode.com/problem/919/
# LeetCode Link - https://leetcode.com/problems/meeting-rooms-ii/

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

from heapq import *

class Meeting:
  def __init__(self, start, end):
      self.start = start
      self.end = end

  def __lt__(self, other):
      # min heap based on meeting.end
      return self.end < other.end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key=lambda x: x.start)

        # Converting to own list of meetings to use function __lt__
        meetings = []
        for i in intervals:
            meetings.append(Meeting(i.start, i.end))

        minRooms = 0
        minHeap = []

        for meeting in meetings:
            # remove all the meetings that have ended
            while (len(minHeap)) > 0 and meeting.start >= minHeap[0].end:
                heappop(minHeap)

            # add the current meeting into min_heap
            heappush(minHeap, meeting)
            # all active meetings are in the min_heap, so we need rooms for all of them 
            minRooms = max(minRooms, len(minHeap))

        return minRooms

'''
Time Complexity - O(nlogn) for sorting
Space Complexity - O(n)
'''
