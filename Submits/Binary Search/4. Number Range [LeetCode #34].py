class Solution:
    def searchRange(self, nums , target):
        result = [-1, -1]
        result[0] = self.binary_search(nums, target, False)
        if result[0] != -1: # no need to search, if 'key' is not present in the input array
            result[1] = self.binary_search(nums, target, True)
        return result
    
    # Modified Binary Search
    def binary_search(self, nums, target, findMaxIndex):
        keyIndex = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:  # key == nums[mid]
                keyIndex = mid
                if findMaxIndex:
                    start = mid + 1  # search ahead to find the last index of 'key'
                else:
                    end = mid - 1  # search behind to find the first index of 'key'

        return keyIndex        

'''
Time Complexity - O(logN)
Space Complexity - O(1)
'''
