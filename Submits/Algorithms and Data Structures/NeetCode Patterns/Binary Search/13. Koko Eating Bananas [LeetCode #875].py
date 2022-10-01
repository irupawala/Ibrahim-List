import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # because max res can be max value of bananas in a pile
        
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
                
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
                
        return res
    
'''
Time Complexity - O(log(MaxP)*len(P))
Space Complexity - O(1)

Notice that brute-force solution is we start from 1,2... and check the min number(speed k) which can finish the consumption of all the banana's within h hours
Time Complexity - O(MaxP*len(P))
'''
