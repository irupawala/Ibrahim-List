'''
class Solution:
    
    def find_j(self, i, k):
        for j in range(i+1, k):
            if self.nums[i] < self.nums[j] and self.nums[k] < self.nums[j]: 
                return True
        return False
            
    def find132pattern(self, nums: List[int]) -> bool:
        self.nums = nums
        for i in range(len(self.nums)):
            for k in range(i+2, len(self.nums)):
                if i+2 < len(self.nums) and nums[i] < nums[k]:
                    if self.find_j(i, k): return True

        return False
        
T - O(n^3)
'''

'''
class Solution:
            
    def find132pattern(self, nums: List[int]) -> bool:
        _min = nums[0]
        for j in range(1, len(nums)-1):
            _min = min(_min, nums[j])
            # if min == nums[j]: continue
            if _min < nums[j]:
                for k in range(j+1, len(nums)):
                    if nums[k] < nums[j] and _min < nums[k]: return True

        return False
        
T - O(n^2)
'''   

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
      
        num_k = -math.inf
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < num_k:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
                num_k = stck.pop()  # this will ensure  num_k < stck[-1] for next iteration

            stck.append(nums[i])
        return False
        