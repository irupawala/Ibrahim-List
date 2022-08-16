# BFS Solution
'''
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        res = [[]]
        last_subset = []
        
        for counter in range(n):
            startIndex = 0
            if counter > 0 and nums[counter] == nums[counter-1]:
                startIndex = endIndex 
            endIndex = len(res)
            for i in range(startIndex, endIndex):
                set1 = res[i][:]
                set1.append(nums[counter])
                res.append(set1)
                last_subset.append(set1) 
        
        return res
'''        
        
# DFS Solution
'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        res = [[]]
        last_subset = []
        
        for counter in range(n):
            startIndex = 0
            if counter > 0 and nums[counter] == nums[counter-1]:
                startIndex = endIndex 
            endIndex = len(res)
            for i in range(startIndex, endIndex):
                set1 = res[i][:]
                set1.append(nums[counter])
                res.append(set1)
                last_subset.append(set1) 
        
        return res

'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''
