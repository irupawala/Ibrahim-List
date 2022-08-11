class Solution:
   
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:  # left side is sorted in ascending order
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:  # target > nums[mid]
                    start = mid + 1
            else:  # right side is sorted in ascending order
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        # we are not able to find the element in the given array
        return -1

'''
Time Complexity - O(logN)
Space Complexity - O(1)
'''
