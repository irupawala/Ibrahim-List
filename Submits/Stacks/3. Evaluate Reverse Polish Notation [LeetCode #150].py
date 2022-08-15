from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        
        for char in tokens:
            if char not in ["+", "-", "*", "/"] :
                q.append(char)
            else:
                no2 = int(q.pop())
                no1 = int(q.pop())
                if char == "+": res = no1 + no2
                if char == "-": res = no1 - no2
                if char == "*": res = no1 * no2
                if char == "/": 
                    if (no1 < 0 and no2 > 0) or (no1 > 0 and no2 < 0): res = math.ceil(no1 / no2)
                    else: res = math.floor(no1 / no2)

                q.append(res)
                
        return int(q[0])

'''
Time Complexity - O(N)
Space Complexity - O(N)
'''
