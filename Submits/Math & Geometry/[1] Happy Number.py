class Solution:
    def isHappy(self, n) :
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)  # move one step
            fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
                break            
        return slow == 1 
        
    def find_square_sum(self, num):
        _sum = 0
        while num > 0:
            _sum += (num % 10)**2
            num //= 10
        return _sum
    
'''
Time Complexity - O(logN)
Space Complexity - O(1)
'''
