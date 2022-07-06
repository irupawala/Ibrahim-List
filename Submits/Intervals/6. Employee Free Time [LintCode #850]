# LintCode Link - https://www.lintcode.com/problem/850/

# LintCode Solution 

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import *

class Solution:
    def employeeFreeTime(self, schedule):
        import heapq
        heap, result = [], []
        for employee in schedule:
            for i in range(0, len(employee), 2):
                heapq.heappush(heap, (employee[i], 0))
                heapq.heappush(heap, (employee[i + 1], 1))
        
        count, n = 0, len(heap)
        while n > 1:
            left = heapq.heappop(heap)
            right = heap[0]
            if (left[1] == 0):
                count += 1
            else:
                count -= 1
            if left[1] == 1 and right[1] == 0:
                if count == 0:
                    result.append(Interval(left[0], right[0]))
            n = len(heap)
        
        return result

'''
Time Complexity - O(nlogn) 
Space Complexity - O(n) to store the data in heap
'''

# Grokking Solution

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import *

class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        # min heap based on start
        return self.interval.start < other.interval.start

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # Write your code here
        if schedule is None:
            return []

        schedule_modified = []

        # generating a sublist for working slots pairs for each employee because each interval is to be assigned intervalIndex
        for employeeSchedule in schedule:
            working_hours = [] # working hours of each employee
            for i in range(0, len(employeeSchedule), 2):
                working_hours.append(Interval(employeeSchedule[i], employeeSchedule[i+1]))
            schedule_modified.append(working_hours)

        n = len(schedule_modified)
        result, minHeap = [], []

        # insert the first interval of each employee to the queue
        for i in range(n):
            #print(schedule_modified[i][0].start)
            #print(schedule_modified[i][0].end)
            heappush(minHeap, EmployeeInterval(schedule_modified[i][0], i, 0))
       
        previousInterval = minHeap[0].interval

        while minHeap:
            queueTop = heappop(minHeap)

                # if previousInterval is not overlapping with the next interval, insert a free interval
            if previousInterval.end < queueTop.interval.start:
                result.append(Interval(previousInterval.end, queueTop.interval.start))
                previousInterval = queueTop.interval

            # overlapping intervals, update the previousInterval if needed
            else:
                if previousInterval.end < queueTop.interval.end:
                    previousInterval = queueTop.interval

            # if there are more intervals available for the same employee, add their next interval
            employeeSchedule = schedule_modified[queueTop.employeeIndex]
            if len(employeeSchedule) > queueTop.intervalIndex + 1:
                heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                                queueTop.intervalIndex + 1))
        
        return result

'''
Time Complexity - O(nlogk), where n is total number of intervals and k is total number of employees
Space Complexity - O(k), because at anytime we will not have more than k elements in heap 
'''
