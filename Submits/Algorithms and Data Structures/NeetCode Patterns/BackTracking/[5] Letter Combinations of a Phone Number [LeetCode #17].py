# LeetCode Link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        result = []
        mapping = {
                   "2": ["a", "b", "c"],
                   "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"],
                   "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"],
                   "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"],
                   "9": ["w", "x", "y", "z"]                 
                  }
        
        def dfs(subset, i):
            if len(subset) == len(digits):
                result.append("".join(map(str, subset)))
                return 
            
            for letter in mapping[digits[i]]:
                subset.append(letter)
                dfs (subset, i+1)
                subset.pop()
        
        dfs([], 0)
        return result
    
'''
Time Complexity - O(4^n), where n is length of digits
Space Complexity - O(n) for the recursion stack
'''
