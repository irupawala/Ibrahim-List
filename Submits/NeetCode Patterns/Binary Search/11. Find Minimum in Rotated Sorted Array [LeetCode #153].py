class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m] < nums[r]:
                r = m           

            elif nums[m] > nums[l]:
                l = m

            if r - l <= 1:
                break

        if nums[l] < nums[r]: return nums[l]
        else: return nums[r]
        
'''
Time Complexity - O(logn)
Space Complexity - O(1)
'''
