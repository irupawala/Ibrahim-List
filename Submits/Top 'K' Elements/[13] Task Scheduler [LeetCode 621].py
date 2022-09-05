# NeetCode Solution
'''
from heapq import *
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        #count = {x:tasks.count(x) for x in set(tasks)}
        maxHeap = [(-cnt) for cnt in count.values()]
        heapify(maxHeap)
        
        q = deque() # pairs of [-cnt, idleTime]
        
        time = 0
        while maxHeap or q:
            time += 1
            
            if not maxHeap: # If there are elements in heap process it first before going to next iteration of same                               # task or inserting an idle time
                time = q[0][1]
            else:
                cnt = 1 + heappop(maxHeap)
                if cnt: # because if cnt becomes 0 no need to add it back in q
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time
'''

#S = Solution()
#print(S.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
#print(S.leastInterval(["A","A","A","B","B","B"], 2))

'''
Time Complexity - O(logn) = O(log26) for stack and O(n) for counting each values
Space Complexity - O(n) for heap and queue
'''    


# Grokking Solution
from heapq import *


class Solution:
    def leastInterval(self, tasks, k):
        intervalCount = 0
        taskFrequencyMap = {}
        for char in tasks:
            taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

        maxHeap = []
        # add all tasks to the max heap
        for char, frequency in taskFrequencyMap.items():
            heappush(maxHeap, (-frequency, char))

        while maxHeap:
            waitList = []
            n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
            while n > 0 and maxHeap:
                intervalCount += 1
                frequency, char = heappop(maxHeap)
                if -frequency > 1:
                    # decrement the frequency and add to the waitList
                    waitList.append((frequency+1, char))
                n -= 1

            # put all the waiting list back on the heap
            for frequency, char in waitList:
                heappush(maxHeap, (frequency, char))

            if maxHeap:
                intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

        return intervalCount    

'''
Time Complexity - O(N.logN)
Space Complexity - O(N)
'''
    
    
