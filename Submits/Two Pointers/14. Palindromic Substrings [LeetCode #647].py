# LeetCode Link - https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        
        def checkPalindrome(l, r, resLen):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    #res = s[l:r+1]
                    resLen = r-l+1
                    self.count += 1
                l -= 1
                r += 1
            
            
        for i in range(len(s)):       
            checkPalindrome(i, i, 0) # odd length
            checkPalindrome(i, i+1, 0) # even length       
        return self.count        

'''
Time Complexity - O(n.n)
Space Complexity - O(1)
'''
