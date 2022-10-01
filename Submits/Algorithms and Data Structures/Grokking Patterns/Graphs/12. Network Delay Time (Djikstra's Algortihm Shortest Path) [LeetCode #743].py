# LeetCode Link - https://leetcode.com/problems/network-delay-time/

#Djikstra's Algorithm - Shortest Path

from heapq import *

class Solution:
    def networkDelayTime(self, times, n, k):
        visited = set()
        dist = {i+1: float("inf") for i in range(n)}
        adj_list = {i+1: [] for i in range(n)}
        
        for u, v, cost in times:
            adj_list[u].append((v, cost)) # Adj_list contains (nei, cost)
        
        dist[k] = 0
        minHeap = []
        heappush(minHeap, [0, k]) # pushing (dist, node) to minHeap
        
        while minHeap:
            min_cost, node = heappop(minHeap)
            if len(visited) == n: break
            if node not in visited:
                visited.add(node)
                for nei, cost_nei in adj_list[node]:
                    if dist[nei] > dist[node] + cost_nei:
                        dist[nei] = dist[node] + cost_nei
                        heappush(minHeap, (dist[nei], nei))
                    
        return max(dist.values()) if len(visited) == n else -1


# NeetCode Solution 
'''
from heapq import *

class Solution:
    def networkDelayTime(self, times, n, k):
        visited = set()
        adj_list = {i+1: [] for i in range(n)}
        
        for u, v, cost in times:
            adj_list[u].append((v, cost)) # Adj_list contains (nei, cost)
        
        minHeap = []
        heappush(minHeap, (0, k)) # pushing (dist, node) to minHeap
        result = 0
        
        while minHeap:
            min_cost, node = heappop(minHeap)
            if node not in visited:
                result = max(result, min_cost)
                visited.add(node)
                for nei, cost_nei in adj_list[node]:
                    heappush(minHeap, (min_cost+cost_nei, nei))

        return result if len(visited) == n else -1 
'''


'''
Time Complexity - Elog(V)
Space Complexity - |V| + |V| ~= |V| to store adjacency list
'''
