'''
Grokking - https://leetcode.com/problems/minimum-height-trees/
'''

from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        #a. Define adj list and inDegrees
        adj_list = {i:[] for i in range(n)}
        inDegree = {i:0 for i in range(n)}
        
        #b. Create the graph
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            inDegree[a] += 1
            inDegree[b] += 1
            
        #c. load the leaves in to the sources
        sources = deque()
        for i in inDegree:
            if inDegree[i] == 1:
                sources.append(i)
                
        #d. Prune the leaves and add new leaves till 1 or 2 root nodes are found
        nodes_count = n
        result = []
        while sources:
            if nodes_count <= 2: 
                while sources: 
                    x = sources.popleft()
                    result.append(x)
            else:
                for _ in range(len(sources)):
                    vertex = sources.popleft()
                    nodes_count -= 1
                    inDegree[vertex] -= 1
                    for nei in adj_list[vertex]:
                        inDegree[nei] -= 1
                        if inDegree[nei] == 1:
                            sources.append(nei)
        return result
                    
S = Solution()
print(S.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
                    
            
'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|)
'''        
