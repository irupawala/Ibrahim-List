class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums) # Important to reduce the time complexity
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet: #Important to begin from the start of the list
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
'''
Time Complexity - O(n)
Space Complexity - O(n)
'''

'''
S = Solution()
print(S.longestConsecutive([100,4,200,1,3,2]))
'''
