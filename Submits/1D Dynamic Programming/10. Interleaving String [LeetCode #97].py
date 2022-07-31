# LeetCode Link - https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

'''
Time Complexity - O(n.m)
Space Complexity - O(n.m)
'''


'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {}
        # k = i + j
        def dfs(i, j):
            if i == len(s1) and j == len(s2): return True
            if (i, j) in dp:
                return dp[(i,j)]
            
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j): return True # if s1[i]==s3[i+j] then it means we're using char at position i and now check if the remaining char of s1 that is i+1(sub-problem) returns True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1): return True
            # No need for caching, if we find one valid result we can immediately return true
            
            # Cache the (i,j) if neither of the above returns True
            dp[(i,j)] = False
            return False
        return dfs(0, 0)
'''
    
