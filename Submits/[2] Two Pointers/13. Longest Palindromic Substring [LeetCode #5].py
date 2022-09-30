# LeetCode Link - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        def checkPalindrome(l, r, res):
            resLen = len(res)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
            return res
            
            
        for i in range(len(s)):       
            # odd length
            l, r = i, i
            res = checkPalindrome(l, r, res)
            # even length    
            l, r = i, i+1
            res = checkPalindrome(l, r, res)        
        return res


'''
Time Complexity - O(n.n)
Space Complexity - O(1)
'''
