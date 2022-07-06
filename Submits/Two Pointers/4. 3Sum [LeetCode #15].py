# LeetCode Link - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        nums.sort()
        self.nums = nums
        self.res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue # to avoid duplicates
            self.two_sum_zero(i, i+1)
        return self.res
            
    def two_sum_zero(self, i, left):
        target_sum = 0 - self.nums[i]
        right = len(self.nums)-1
        
        while left < right:              
            _sum = self.nums[left] + self.nums[right]
            
            if _sum == target_sum: 
                self.res.append([self.nums[i], self.nums[left], self.nums[right]]) 
                left += 1
                
                while self.nums[left] == self.nums[left-1] and left < right: # necessary to avoid duplicates, right will take care of itself 
                    left += 1
                #right -= 1
                #while self.nums[right] == self.nums[right+1] and left < right:
                #    right -= 1

            if _sum < target_sum:
                left += 1
                
            elif _sum > target_sum:
                right -= 1
                
        return None       
        
'''
Time Complexity - NlogN + N^2
Space Complexity - O(N) for sorting
'''        
