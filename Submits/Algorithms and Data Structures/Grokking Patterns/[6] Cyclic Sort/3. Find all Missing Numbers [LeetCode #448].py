class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        missingNumbers = []
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                missingNumbers.append(i+1)
                
        return missingNumbers
                
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
