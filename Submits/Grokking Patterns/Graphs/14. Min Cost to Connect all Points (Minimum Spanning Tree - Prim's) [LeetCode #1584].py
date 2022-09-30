LeetCode Link - https://leetcode.com/problems/min-cost-to-connect-all-points/

from heapq import *
# Prim's Algorithm

class Solution:
    def minCostConnectPoints(self, points) :
        visited = set()
        distance = {i:{} for i in range(len(points))} # distance[source[destination]] = dist
        result = 0
        
        # populate the distance
        for i, coordinates_1 in enumerate(points):
            for j, coordinates_2 in enumerate(points):
                if i != j:
                    x1, y1 = coordinates_1[0], coordinates_1[1]
                    x2, y2 = coordinates_2[0], coordinates_2[1]
                    dist = abs(x1-x2) + abs(y1-y2)
                    distance[i][j] = dist
        
        minHeap = []
        heappush(minHeap, (0,0)) # (dist, node)
        
        while minHeap:
            if len(visited) == len(points): break
            min_dist, point = heappop(minHeap)
            if point not in visited:
                visited.add(point)
                result += min_dist
                for nei in distance[point]:
                    if nei not in visited:
                        heappush(minHeap, (distance[point][nei], nei))
                    
        return result

'''
Time Complexity - O(|V|^2) + O(|E|log|V|), V^2 for populating distance, |E|log|V| for Prim's Algorithm
Space Complexity - O(|V|^2)
'''
