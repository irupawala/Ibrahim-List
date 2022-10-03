# LeetCode Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Variable length with fixed length HashMap as the length modifying criteria  

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string_len, i = 0, 0
        substring = []

        while i < len(s):        
            if s[i] not in substring :
                substring.append(s[i])              
            else: 
                i = i - len(substring) 
                substring = []
            i += 1
            max_string_len = max(max_string_len, len(substring))   

        return max_string_len   
'''
    
    
'''
Time Complexity - O(n^2)
Space Complexity - O(n)
'''

# Neet Code O(n) Solution
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
'''

'''
Time Complexity - O(n2)
Space Complexity - O(n)
'''

# Grokking Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        char_index_map = {}

        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(s)):
            right_char = s[window_end]
            # if the map already contains the 'right_char', shrink the window from the beginning so that
            # we have only one occurrence of 'right_char'
            if right_char in char_index_map:
              # this is tricky; in the current window, we will not have any 'right_char' after its previous index
              # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
                window_start = max(window_start, char_index_map[right_char] + 1)
            # insert the 'right_char' into the map
            char_index_map[right_char] = window_end
            # remember the maximum length so far
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length        
