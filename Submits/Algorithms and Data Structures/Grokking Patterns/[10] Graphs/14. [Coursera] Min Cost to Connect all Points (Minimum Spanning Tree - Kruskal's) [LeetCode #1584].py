# LeetCode Link - https://leetcode.com/problems/min-cost-to-connect-all-points/

from heapq import *
# Kruskal's Algorithm

class Solution:
    def minCostConnectPoints(self, points) :
        edges_length, edges_count = len(points)-1, 0
        parents = [i for i in range(len(points))]
        result = 0
    
        
        # populate the distance
        minHeap = []
        for i, coordinates_1 in enumerate(points):
            for j, coordinates_2 in enumerate(points):
                if i != j:
                    x1, y1 = coordinates_1[0], coordinates_1[1]
                    x2, y2 = coordinates_2[0], coordinates_2[1]
                    dist = abs(x1-x2) + abs(y1-y2)
                    heappush(minHeap, [dist, (i, j)] ) # (dist, (u,v))        
        
        def find(n):
            while n != parents[n]:
                parents[n] = find(parents[n]) # Path Compression Heuristics
                n = parents[n]
            return n
        
        def union(n1, n2):
            parents1, parents2 = find(n1), find(n2)
            
            if parents1 != parents2: # Not using union by Rank Heuristics
                parents[parents1] = parents2
                return True
            return False
                
                
        while minHeap:
            if edges_length == edges_count: break
                
            min_dist, coordinates = heappop(minHeap)
            n1, n2 = coordinates[0], coordinates[1]
            if union(n1, n2):
                result += min_dist
                edges_count += 1
        return result

'''
Time Complexity - O(V^2.logV) + |E|.logV V2logV for pushing the diff in Heap. |E|log|V| for Kruskal's
Space Complexity - O(V^2) for Edges
'''
