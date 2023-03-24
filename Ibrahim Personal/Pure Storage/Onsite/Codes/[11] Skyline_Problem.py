from heapq import *

class Solution:
    def getSkyline(self, buildings):
        points = []
        result = []
        currentMaxHeight = 0
        maxHeap = [0] # Initializing heap with 0 to record the first point
        
        for start, end, height in buildings:
            points.append([start, -height]) # When two buildings have same start then the one with more height should be processed first because the point with lower height is not a valid point. This way CurrentMaxHeight will be set to the higher height.
            points.append([end, height]) # When two buildings have same end then the one with lower height should be processed first so that it gets removed first and then the one with higher height gets processed as it is the valid point
        
        points.sort()   
        for x, height in points:
            if height < 0: # x is start
                heappush(maxHeap, height)
            else: # x is end, this means building has ended hence remove it from the heap
                maxHeap.remove(-height)
                heapify(maxHeap)
                '''
                ind = maxHeap.index(-height)
                maxHeap[ind] = maxHeap[-1]
                del maxHeap[-1]
                if ind < len(maxHeap):
                    heapq._siftup(maxHeap, ind)
                    heapq._siftdown(maxHeap, 0, ind)  
                '''

            if currentMaxHeight != -maxHeap[0]: # Max got changed hence point should be recorded in the output
                currentMaxHeight = -maxHeap[0]
                result.append([x, currentMaxHeight])
                
        return result
        
'''
Time Complexity - O(n) (populating points) + O(nlogn) (Sort) + O(n/2)logn (push) + O(n/2)(n) (remove) =~ O(n**2)
Space Complexity - O(n) (points) + O(n) (heap) =~ O(n)
'''