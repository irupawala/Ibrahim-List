LeetCode Link - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, i, right = 0, 0, len(nums)-1
        
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
                
            elif nums[i] == 1:
                i += 1
                
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

            #print(f"i = {i}, left = {left}, right = {right}, nums = {nums}")
        return nums
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''

