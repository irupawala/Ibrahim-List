# LeetCode Link - https://leetcode.com/problems/redundant-connection/

# NeetCode Solution

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


'''
# Ibrahim Solution 
class Solution:
    def findRedundantConnection(self, edges):
        parents = [i for i in range(len(edges)+1)] # Notice that we are not going to use index 0
        rank = [0] * (len(edges)+1)
        
        def find(n):
            while n != parents[n]:
                #parents[n] = parents[parents[n]] # Path Compression Heuristics
                #parents[n] = find(parents[n]) # Path Compression Heuristics
                n = parents[n]
            return n
                
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: return False
            
            parents[p1] = p2
            
            
            '''
            if rank[p1] > rank[p2]: # Union by Rank Heuristics
                parents[p2] = p1
            else:
                parents[p1] = p2
                if rank[p1] == rank[p2]:
                    rank[p2] += 1
                    
            '''
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

#S = Solution()
#print(S.findRedundantConnection([[1,2],[1,3],[2,3]]))
'''

'''
Time Complexity - O(logn)
Space Complexity - O(n) for storing parents and rank
'''