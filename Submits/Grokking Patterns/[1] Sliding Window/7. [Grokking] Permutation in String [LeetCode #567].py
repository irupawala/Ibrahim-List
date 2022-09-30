# LeetCode Link - https://leetcode.com/problems/permutation-in-string/
# Variable length Window requiring match of all chars in a HashMap

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequency = {}
        window_start = 0
        
        
        # create the count of letters in s1
        for c in s1:
            char_frequency[c] = char_frequency.get(c, 0) + 1
         
        matched = len(char_frequency) # len of the string s1
        #print(char_frequency)
            
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            
            if right_char in char_frequency:
                char_frequency[right_char] -= 1

                if char_frequency[right_char] == 0:
                    matched -= 1
                    
                #print(f"right_char = {right_char}, matched = {matched}")
                    
                if matched == 0: return True      
                
            if window_end >= len(s1)-1:
                left_char = s2[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched += 1                        
                    char_frequency[left_char] += 1

        return False

'''
Time Complexity - O(N+M)
Space Complexity - O(M)
'''     
