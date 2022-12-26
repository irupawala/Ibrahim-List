# LeetCode Link - https://leetcode.com/problems/generate-parentheses/

#BFS Solution
from collections import deque

class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

class Solution:

    def generateParenthesis(self, num):
        result = []
        queue = deque()
        queue.append(ParenthesesString("", 0, 0))
        while queue:
            ps = queue.popleft()
            # if we've reached the maximum number of open and close parentheses, add to the result
            if ps.openCount == num and ps.closeCount == num:
                result.append(ps.str)
            else:
                if ps.openCount < num:  # if we can add an open parentheses, add it
                    queue.append(ParenthesesString(ps.str + "(", ps.openCount + 1, ps.closeCount))

                if ps.openCount > ps.closeCount:  # if we can add a close parentheses, add it
                    queue.append(ParenthesesString(ps.str + ")", ps.openCount, ps.closeCount + 1))

        return result     

# Ibrahim Solution 

'''    
    def generateParenthesis(self, n):
        result = []
        q = deque()
        q.append("(")
        for counter in range(2*n):
            len_q = len(q)
            for i in range(len_q):
                brac = list(q.popleft())
                openCount, closedCount = brac.count("("), brac.count(")")
                if openCount < n:
                    openbrac = list(brac)
                    openbrac.append("(")
                    open_str = "".join(openbrac)
                    q.append(open_str)
                    if len(open_str) == 2*n: result.append(open_str)
                if closedCount < openCount:
                    closedbrac = list(brac)
                    closedbrac.append(")")
                    closed_str = "".join(closedbrac)
                    q.append(closed_str)
                    if len(closed_str) == 2*n: result.append(closed_str)
        
        return result
'''

# DFS Solution
'''
class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
'''    

'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''