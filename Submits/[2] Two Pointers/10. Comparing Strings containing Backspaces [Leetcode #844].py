# LeetCode Link - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s, t):
        # use two pointer approach to compare the strings
        index1 = len(s) - 1
        index2 = len(t) - 1
        while (index1 >= 0 or index2 >= 0):
            i1 = self.get_next_valid_char_index(s, index1)
            i2 = self.get_next_valid_char_index(t, index2)
            if i1 < 0 and i2 < 0:  # reached the end of both the strings
                return True
            if i1 < 0 or i2 < 0:  # reached the end of one of the strings
                return False
            if s[i1] != t[i2]:  # check if the characters are equal
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True


    def get_next_valid_char_index(self, str, index):
        backspace_count = 0
        while (index >= 0):
            if str[index] == '#':  # found a backspace character
                backspace_count += 1
            elif backspace_count > 0:  # a non-backspace character
                backspace_count -= 1
            else:
                break

            index -= 1  # skip a backspace or a valid character

        return index
    
'''
Time Complexity - O(N+M)
Space Complexity - O(1)
'''
