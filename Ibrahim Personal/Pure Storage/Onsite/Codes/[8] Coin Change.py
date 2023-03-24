class Solution:
    def coinChange(self, coins, amount) :
        dp = [None for i in range(amount+1)]
        dp[0] = 0
        
        for total in range(1, amount+1):
            dp[total] = float("inf")
            for coin in coins:
                if coin <= total:
                    min_coins = dp[total-coin] + 1
                    if min_coins < dp[total]:
                        dp[total] = min_coins

                    
        #print(dp)            
        if dp[amount] == float("inf"): return -1
        return dp[amount]
        
'''
Time Complexity - O(n)
Space Complexity - O(n)
'''