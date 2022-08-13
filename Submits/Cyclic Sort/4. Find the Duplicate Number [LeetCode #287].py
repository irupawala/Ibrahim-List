class Solution:
    def findDuplicate(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if i != j and nums[i] == nums[j]: return nums[i]
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        return -1
        
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
