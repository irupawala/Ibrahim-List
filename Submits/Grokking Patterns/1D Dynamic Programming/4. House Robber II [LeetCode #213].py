# LeetCode Link - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums) -> int:
        
        if len(nums) < 3: return max(nums)
        return max( self.robber_old(nums[1:]), self.robber_old(nums[:-1]) )

    def robber_old(self, nums: List[int]) -> int:

        dp = [0 for i in range(len(nums)+1)]
        dp[1] = nums[0]
        
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], (dp[i-2]+nums[i-1])) # max of (uptill previous house dp[i-1] or current nums[i-1] + previous to previous dp[i-1])
                        
        return dp[len(nums)]

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
