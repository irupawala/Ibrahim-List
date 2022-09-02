# Ibrahim Solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        
        dp[len(nums)-1] = 0
        
        for i in range(len(nums)-2, -1, -1):
            minJumpLen = float("inf")
            for j in range(i+1, i+nums[i]+1):
                if j < len(nums):
                    minJumpLen = min(minJumpLen, 1+dp[j])
            dp[i] = minJumpLen
            
        return dp[0]
        

# NeetCode Solution
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
'''

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
