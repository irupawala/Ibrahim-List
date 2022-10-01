from collections import deque

class Solution:
# BFS Solution
    def isBipartite(self, graph):
        color = {}
        
        for i in range(len(graph)):
            if i not in color:
                q = deque()
                q.append(i)
                color[i] = 0

                while q:
                    i = q.popleft()

                    for j in graph[i]:
                        if j in color:
                            if color[j] == color[i]: return False
                        else:
                            color[j] = 1 - color[i]
                        q.append(j)
        return True

    
# Union-Find Solution
    ''' 
    def isBipartite(self, graph) -> bool:
        #write your code here
        parents = [i for i in range(len(graph))]
        rank = [0]* (len(graph))
        
        def find(n):
            while n != parents[n]:
                parents[n] = parents[parents[n]] # Path Compression Heuristics
                #parents[n] = find(parents[n])
                n = parents[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            #if p1 != p2: parents[p1] = p2 # without Union by Rank Heuristics
            
            if p1 != p2:     
                if rank[p1] > rank[p2]: #Union by Rank Heuristics
                    parents[p2] = p1
                else:
                    parents[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p1] += 1
            

        
        for i in range(len(graph)):
            par_i = find(i)
            for j in graph[i]:
                if find(j) == par_i: return False
                union(graph[i][0], j)
                
        #print(parents)
        return True
        ''' 

    
# DFS Solution
'''
    def isBipartite(self, graph):
        color = {}
        
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]: return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i): return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i): return False
        return True
'''

'''
Time Complexity - O(n) for each approach
Space Complexity - Depends on approach
'''

