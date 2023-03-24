class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        a, b = 0, 1
        for i in range(2, n+1):
            result = a + b
            a = b
            b = result
            
        return result
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''