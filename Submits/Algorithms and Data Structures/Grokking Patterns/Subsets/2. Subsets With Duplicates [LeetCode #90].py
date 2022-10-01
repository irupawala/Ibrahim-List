# DFS Solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res       
        
# BFS Solution
'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''

'''
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        res = [[]]
        
        for counter in range(n):
            startIndex = 0
            if counter > 0 and nums[counter] == nums[counter-1]:
                startIndex = endIndex 
            endIndex = len(res)
            for i in range(startIndex, endIndex):
                set1 = res[i][:]
                set1.append(nums[counter])
                res.append(set1)
        
        return res
'''

'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''
