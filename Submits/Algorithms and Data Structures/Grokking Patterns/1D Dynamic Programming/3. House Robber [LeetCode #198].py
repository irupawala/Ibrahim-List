class Solution:
    def rob(self, nums) -> int:
        dp = [0 for i in range(len(nums)+1)]
        dp[1] = nums[0]
        
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], (dp[i-2]+nums[i-1])) # max of (uptill previous house dp[i-1] or current nums[i-1] + previous to previous dp[i-1])
                        
        return dp[len(nums)]

# As we need only last two dp values dp[i-1] and dp[i-2], this problem can be solved using just two parameters

# NeetCode Solution

'''
class Solution:
    # [rob1, rob2 n, n+1, ......] 
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0 # rob, rob2 are max till that index 
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    

# Recurrence Relation - rob = max(arr[0]+rob[2:n], rob[1:n]) #We can rob at position 0 & [2:n] or position [1:n]

S = Solution()
print(S.rob([2,14,9,3,1]))
'''

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
