# LeetCode Link - https://leetcode.com/problems/word-break/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''