LeetCode Link - https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums):
        left = 0
        right = len(nums)-1

        # find the first number out of sorting order from the beginning
        while (left < len(nums) - 1 and nums[left] <= nums[left + 1]):
            left += 1
        
        if left == len(nums)-1: return 0 # Already sorted  
        
        # find the first number out of sorting order from the end
        while (right > 0 and nums[right] >= nums[right - 1]):
            right -= 1
        
        # find the maximum and minimum of the subarray
        subarray_max = float("-inf")
        subarray_min = float("inf")
        for k in range(left, right+1):
            subarray_max = max(subarray_max, nums[k])
            subarray_min = min(subarray_min, nums[k])
        
        
        while left > 0 and nums[left-1] > subarray_min:
            left -= 1
            
        while right < len(nums)-1 and nums[right+1] < subarray_max:
            right += 1
            
        return right - left + 1 
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
