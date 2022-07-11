LeetCode Link - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        window_sum = 0
        window_start = 0
        for window_end in range(0, len(nums)):
            window_sum += nums[window_end]  # add the next element
            # shrink the window as small as possible until the 'window_sum' is smaller than 's'
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
      
        if min_length == float("inf"):
            return 0
        return min_length
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
