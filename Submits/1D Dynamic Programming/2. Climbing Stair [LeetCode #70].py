# LeetCode Link - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        result = [None for x in range(n+1)]
        result[0] = 1
        
        for index in range(1, len(result)):
            ways = 0
            for s in steps:
                if index - s >= 0:
                    ways += result[index-s]
            result[index] = ways
            
        return result[len(result)-1]
            
        
'''
Time Complexity - O(n)
Space Complexity - O(n)
Note that it can also be solved using two variables, please see the solution by NeetCode below
'''

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        n1, n2 = 2, 3
        
        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
'''
