
# Using Cyclic Sort
class Solution:
    def missingNumber(self, nums):
        i, n = 0, len(nums)
        
        while i < n:
            j = nums[i]
            if j < n and nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i: return i
        
        return len(nums)


'''
# Using Sum[range] - Sum[nums] = Missing Num
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _total = sum(range(len(nums)+1))
        return _total - sum(nums)      
'''

'''
# Using XOR Method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _total_XOR = 0
        for i in range(len(nums)+1): _total_XOR ^= i
        for j in nums: _total_XOR ^= j
            
        return _total_XOR
'''

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
