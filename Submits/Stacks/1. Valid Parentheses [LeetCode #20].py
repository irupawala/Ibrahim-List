# Solution 1

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = deque()

        for i in s:
            if i in ['(', '{', '[']: stack.append(i)  

            else:
                if not len(stack): return False # for s = "}]"                   
                x = stack.pop()
                if (x=="(" and i!=")") or (x=="{" and i!="}") or (x =="[" and i!="]"): return False

        return (len(stack) == 0)  # for s = "{["

# Solution 2

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Write your code here
        for i in range(len(s)//2):
            s=s.replace('()','').replace('[]','').replace('{}','')
        return len(s) == 0

      
# Solution 3


class Solution:
    def isValid(self, s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack
    
'''
S = Solution()
print(S.isValid("()[]{}"))
'''        
     
