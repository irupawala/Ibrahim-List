class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        i = 0
        result = None
        smallest_diff = float('inf')
        
        for i in range(0, len(nums)-2):
            
            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue              
            
            left = i+1
            right = len(nums)-1
            
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]

                if _sum == target:
                     return _sum

                diff = target - _sum
                if abs(diff) < smallest_diff:
                    smallest_diff = abs(diff)
                    result = _sum
                    
                if diff > 0:
                    left += 1
                else:
                    right -= 1
                
        return result
                
'''
Time Complexity - O(N.logN + N^2)
Space Complexity - O(N) for sorting
'''
