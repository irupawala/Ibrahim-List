class Solution:
    def characterReplacement(self, s, k) -> int:
        window_start, max_length, longest_char_length = 0, 0, 0
        char_frequency = {}
        
        # try to extend the range till mismatch count is less than k
        for window_end in range(len(s)):
            right_char = s[window_end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1
            
            # update the longest_char_length
            longest_char_length = max(longest_char_length, char_frequency[right_char])
            
            # calculate mismatch length
            mismatch_length = (window_end - window_start + 1) - longest_char_length
            
            # shrink the window till mismatch length is less than k
            while mismatch_length > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                # increase the window
                window_start += 1
                
                
                # find longest char again 
                # longest_char, longest_char_length = max(char_frequency.items(), key = lambda x: x[1])
                
                # notice that this upper line was the major reason for decrease in speed. we do not need to find the longest_char length in each step
                
                # Since we are only interested in the longest valid substring, our sliding windows do not have to shrink, even if a window may cover an invalid substring. Either we expand the window by appending a character to the right or we shift the entire window to the right by one. We only expand the window when the frequency of the newly added character exceeds the historical maximum frequency (from a previous window that included a valid substring).In other words, we do not need to know the exact maximum count of the current window. The only thing we need to know is whether the maximum count exceeds the historical maximum count, and that can only happen because of the newly added char.
                
                # update the mismatch_length
                mismatch_length = (window_end - window_start + 1) - longest_char_length
                
            
            max_length = max(max_length, window_end-window_start+1)
        return max_length
            
'''
Time Complexity - O(N)
Space Complexity - As we expect only the lower case letters in the input string, we can conclude that the space complexity will be O(26) to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1)
'''
