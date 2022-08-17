from collections import deque

class Solution:
    def letterCasePermutation(self, s):
        q = deque()
        q.append(s)
        i, n = 0, len(s)
        
        for i in range(n): # Index i whose case needs to be changed
            if s[i].isalpha():
                len_q = len(q)
                for j in range(len_q):
                    new_str = list(q[j])
                    new_str[i] = new_str[i].swapcase()
                    q.append("".join(new_str))
                
        return list(q)

'''
S = Solution()
print(S.letterCasePermutation("ab7c"))
'''

'''
Time Complexity - O(N.2^N)
Space Complexity - O(N.2^N)
'''
