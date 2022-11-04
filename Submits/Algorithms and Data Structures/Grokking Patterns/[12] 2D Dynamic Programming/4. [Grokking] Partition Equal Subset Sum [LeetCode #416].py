# LeetCode Link - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums):
        if sum(nums)%2 == 1: return False
        
        subset_sum = sum(nums) // 2
        
        dp = [False for _ in range(subset_sum + 1)] # Single Column Solution
        dp[0] = True
        
        for subset in range(1, len(nums)+1):
            for _sum in range(subset_sum, -1, -1): # Single Column hence going in reverse direction
                if nums[subset-1] <= _sum:
                    dp[_sum] = dp[_sum] or dp[_sum-nums[subset-1]] # include the element 
                else:
                    dp[_sum] = dp[_sum] # exclude the element

                if _sum == subset_sum and dp[_sum]: return True # Return as soon as one subset is equal to sum//2
        return False

'''
Time Complexity - O(N.S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
Space Complexity - O(S)
'''
