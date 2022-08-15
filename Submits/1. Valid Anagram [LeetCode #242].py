class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s, set_t = set(list(s)), set(list(t))
        if len(set_s) != len(set_t): return False

        count_s, count_t = {}, {}
        for i in set_s: 
            count_s[i], count_t[i] = s.count(i), t.count(i)
            
        for i in set_s:
            if i not in set_t: return False
            if count_s[i] != count_t[i]: return False
            
        return True
        
        
# Time Complexity - O(n) + O(n) ~= O(n)
