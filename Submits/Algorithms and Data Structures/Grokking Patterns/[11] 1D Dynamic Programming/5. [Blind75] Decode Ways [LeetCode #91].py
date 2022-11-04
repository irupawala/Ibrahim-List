# LeetCode Link - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 } # for empty string and string of len 1 we want to return 1
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == "0":
                dp[i] = 0 # because string cannot start with 0
            else:
                dp[i] = dp[i+1] # for length of first substring 1

                if (i+1< len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))): # for length of first substring 2
                    dp[i] += dp[i+2]
        
        return dp[0]
 
# Memoization Solution 
''' 
class Solution:        
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)        
'''

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
