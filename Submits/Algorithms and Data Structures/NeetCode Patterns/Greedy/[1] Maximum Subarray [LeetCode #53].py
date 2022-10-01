# Ibrahim Solution
class Solution:
    def maxSubArray(self, nums):
        for i in range(len(nums)-2, -1, -1):
            no = nums[i]
            next_no = nums[i+1]
            if no + next_no > no:
                no += next_no
                nums[i] = no
                           
        return max(nums)
    
#S = Solution()
#print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

'''
# Ibrahim Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for val in nums[1 : ]:
            curSum = max(val, curSum + val)
            maxSum = max(maxSum, curSum)
        return maxSum
    


NeetCode Solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
'''

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
