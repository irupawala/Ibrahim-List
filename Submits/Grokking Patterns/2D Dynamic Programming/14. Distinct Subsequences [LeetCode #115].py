class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        
        def dfs(i, j):
            if j == len(t): return 1 # end of t reached means string matches
            if i == len(s): return 0 # end of s reached but not t hence string does not match
            if (i, j) in cache: return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                cache[(i, j)] = dfs(i+1, j)
            return cache[(i, j)]
            
        return dfs(0, 0)
            
'''
Time Complexity - O(m.n)
Space Complexity - O(m.n)
'''
