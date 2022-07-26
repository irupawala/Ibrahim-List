# LeetCode Link - https://leetcode.com/problems/coin-change/

import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for i  in range(amount+1)]
        dp[0] = 0

        for no in range(1, len(dp)):
            dp[no] = math.inf
            for c in coins:
                if no - c >= 0:
                    min_coins = dp[no-c] + 1
                    if min_coins < dp[no]:
                        dp[no] = min_coins

        if dp[amount] == math.inf: return -1            
        return dp[amount]
                

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
