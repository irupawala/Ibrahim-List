class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target-num in nums_dict:
                return [i, nums_dict[target-num]]
            else:
                nums_dict[num] = i

        return [-1, -1]
    
# Time Complexity - O(n)
