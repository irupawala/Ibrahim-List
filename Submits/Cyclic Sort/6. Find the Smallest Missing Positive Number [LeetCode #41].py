class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
