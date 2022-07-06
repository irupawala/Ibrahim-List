LeetCode Link - https://leetcode.com/problems/two-sum/

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

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {index:nums[index] for index in range(len(nums))}
        sorted_dict = {k:v for k, v in sorted(nums_dict.items(), key = lambda item: item[1])}
        sorted_nums_values = list(sorted_dict.values())
        sorted_nums_keys = list(sorted_dict.keys())
        
        pointer_1 = 0
        pointer_2 = len(nums)-1
        
        no_1 = sorted_nums_values[pointer_1]
        no_2 = sorted_nums_values[pointer_2]
         
        while no_1 < no_2:
            if no_1 + no_2 == target: break
            if no_1 + no_2  >= target:
                pointer_2 -= 1
                no_2 = sorted_nums_values[pointer_2]
            else:
                pointer_1 += 1
                no_1 = sorted_nums_values[pointer_1]
            
        return [sorted_nums_keys[pointer_1], sorted_nums_keys[pointer_2]]
'''        

'''
Time Complexity - O(n) + nlog(n)
Space Complexity - O(n) # for storing the dictionary
'''
