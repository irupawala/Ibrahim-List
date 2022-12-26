# LeetCode Link - https://leetcode.com/problems/subsets/

# Using Subsets
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:   
        subsets = []
        # start by adding the empty subset
        subsets.append([])
        for currentNumber in nums:
            # we will take all existing subsets and insert the current number in them to create new subsets
            n = len(subsets)
            for i in range(n):
                # create a new subset from the existing subset and insert the current element to it
                set1 = list(subsets[i])
                set1.append(currentNumber)
                subsets.append(set1)

        return subsets
'''
'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''

# Using Bit Manipulation
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:    
        subsets = []
        set_size = len(nums)
        power_set_size = 2**set_size
        
        for i in range(power_set_size):
            sublist = []
            for j in range(set_size):
                if (i & (1 << j)) > 0:
                    sublist.append(nums[j])
            subsets.append(sublist)
            
        return subsets
'''  
'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''

# Using Back-Tracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:    
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # Do not include nums[i]
            subset.pop() # backtracking
            dfs(i+1)
            
        dfs(0)
        return res
'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''        
        
