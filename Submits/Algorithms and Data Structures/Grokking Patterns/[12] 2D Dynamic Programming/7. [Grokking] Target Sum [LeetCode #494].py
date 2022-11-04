# LeetCode Link - https://leetcode.com/problems/target-sum/

# Using Memoization

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memoization = {} #(index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memoization:
                return memoization[(i,total)]
            
            memoization[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return memoization[(i, total)]
        return backtrack(0, 0)
    
'''
Time Complexity - 2^n
Space Complexity - O(n*total(nums))
'''

# Using Memoization and Nested Dictionaries

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memoization = {} #(index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if i in memoization and total in memoization[i]:
                return memoization[i][total]
            
            res = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            if i in memoization:
                memoization[i][total] = res
            else:
                memoization[i] = {total: res}
            return res
        
        return backtrack(0, 0)
    
'''
Time Complexity - 2^n
Space Complexity - O(n*total(nums))
'''

# Using Dynamic Programming (Only works for Positive Integers (No zero and negative integers)

def find_target_subsets(num, s):
    totalSum = sum(num)

    # if 's + totalSum' is odd, we can't find a subset with sum equal to '(s +totalSum) / 2'
    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0

    return count_subsets(num, (s + totalSum) // 2)


# this function is exactly similar to what we have in 'Count of Subset Sum' problem
def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum+1)]
    dp[0] = 1

    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, sum+1):
        dp[s] = 1 if num[0] == s else 0

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]

    return dp[sum]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()

'''
Time Complexity - O(N∗S), where ‘N’ represents total numbers and ‘S’ is the desired sum.
Space Complexity - O(S)
'''
