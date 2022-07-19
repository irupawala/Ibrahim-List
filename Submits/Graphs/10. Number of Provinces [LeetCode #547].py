class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        weight = [1] * n
        rank = [0] * n
        
        def find(n1):
            res = n1
            
            while res != par[res]:
                par[res] = par[par[res]] # path compression heuristics
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]: #union by rank heuristic
                par[p2] = p1
                weight[p1] += weight[p2]
            else:
                par[p1] = p2
                weight[p2] += weight[p1]
                if rank[p1] == rank[p2]:
                    rank[p2] += 1
            return 1    
        
        total_sets = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    total_sets -= union(i,j)
        
        return total_sets
'''  
Time Complexity - O(|V|+|E|)
Space Complexity - 
'''  
            
            
            
                    
        
