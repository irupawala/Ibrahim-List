https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, i, right = 0, 0, len(nums)-1
        
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                
        return nums
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''