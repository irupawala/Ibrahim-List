class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(len(word1)+1): dp[i][0] = i
        for j in range(len(word2)+1): dp[0][j] = j
        

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                insertion = dp[i][j-1] + 1
                deletion = dp[i-1][j] + 1
                match = dp[i-1][j-1]
                mismatch = dp[i-1][j-1] + 1
                
                if word1[i-1] == word2[j-1]: dp[i][j] = min(insertion, deletion, match)
                else: dp[i][j] = min(insertion, deletion, mismatch)
        
        return dp[i][j]
    
'''
Time Complexity - O(m.n)
Space Complexity - O(m.n)
'''
