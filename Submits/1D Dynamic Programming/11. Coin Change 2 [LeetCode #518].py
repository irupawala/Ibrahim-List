class Solution:
    def change(self, amount, coins) :
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        
        for i in range(len(coins)):
            for a in range(1, amount+1):
                if coins[i] <= a:
                    dp[a] += dp[a-coins[i]]
                    
        return dp[amount]

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
