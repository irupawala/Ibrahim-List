# LeetCode Link - https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Variable length Window requiring match of all chars in a HashMap

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_frequency = {}
        window_start = 0
        result = []
        
        # create the count of letters in p
        for c in p:
            char_frequency[c] = char_frequency.get(c, 0) + 1        
            
        matched = len(char_frequency) # len of the string s1
        #print(char_frequency)
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char in char_frequency:
                char_frequency[right_char] -= 1

                if char_frequency[right_char] == 0:
                    matched -= 1
                    
                #print(f"right_char = {right_char}, matched = {matched}")
                    
                if matched == 0: result.append(window_start)            
                    
            if window_end >= len(p)-1:
                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched += 1                        
                    char_frequency[left_char] += 1     
                    
        return result
    
'''
Time Complexity - O(N+M)
Space Complexity - O(M) for HashMap
'''
