LeetCode Link - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height) -> int:
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right] #maxLeft and maxRight will keep track of maxLeft and maxRight
        result = 0
        
        while left < right:
            if maxLeft < maxRight: # We're moving the max which is minumum between left and right because the amount of water trapped depends on the min height between maxLeft and maxRight
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += (maxLeft - height[left]) # we are supposed to add only positive values to the results as it is not possible to trap negative rain water,
                # however the value won't be negative because we are updating the maxLeft first
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += (maxRight - height[right])
                
        return result
    
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
