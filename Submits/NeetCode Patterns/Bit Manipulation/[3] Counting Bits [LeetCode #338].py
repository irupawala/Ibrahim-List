'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [list(bin(i)).count('1') for i in range(n+1)]
'''


# NeetCode O(n) Solution without the use of any in-built function using DP
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


'''
Time Complexity - O(n)
Space Complexity - O(1) and O(n)
'''
