from collections import deque

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left, product = 0, 1
        #result = []
        
        for right in range(len(nums)):
            product *= nums[right]
            while (product >= k and left <= right):
                product //= nums[left]
                left += 1
                 
            count += (right - left + 1)
            # since the product of all numbers from left to right is less than the target therefore,
            # all subarrays from left to right will have a product less than the target too; to avoid
            # duplicates, we will start with a subarray containing only arr[right] and then extend it  
            '''
            temp_list = deque()
            for i in range(right, left-1, -1):
                temp_list.appendleft(nums[i])
                result.append(list(temp_list))   
            '''
        
        #print(result)
        return count
        
'''
Time Complexity - O(N^2) for count O(N^3) for result
Space Complexity - O(1)
'''
