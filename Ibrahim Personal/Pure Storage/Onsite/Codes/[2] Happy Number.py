# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n) :
        slow, fast = n, n
        while True:
            slow = self.get_square(slow)
            fast = self.get_square(self.get_square(fast))
            if slow == fast:
                break
            
        return slow == 1
    
    def get_square(self, num):
        square = 0
        while num:
            square += (num%10)**2
            num //= 10
            
        return square
    
'''
Time Complexity - O(logN)
Space Complexity - O(1)

1. If the number N is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
2. For N > 1000, suppose the number has ‘M’ digits and the next number is ‘N1’. Now the sum of the squares of the digits of ‘N’ is at most 9^2M  or 81M (this will happen when all digits of ‘N’ are ‘9’).

This means:
1. N1<81M
2. As we know M = log(N+1)
3. Therefore: N1 < 81 * log(N+1) => N1 = O(logN)
This concludes that the above algorithm will have a time complexity of O(logN).
'''