LintCode Link - https://www.lintcode.com/problem/918/

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        # Write your code here
        arr, target_sum = nums, target
        arr.sort()
        count = 0
        for i in range(len(arr)-2):
            count += self.search_pair(arr, target - arr[i], i)
        return count


    def search_pair(self, arr, target_sum, first):
        count = 0
        left, right = first + 1, len(arr) - 1
        while (left < right):
            if arr[left] + arr[right] < target_sum:  # found the triplet
                # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
                # left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1  # we need a pair with a smaller sum
        return count

'''
Time Complexity - O(nlogn) + n^2
Space Complexity - O(n)
'''
