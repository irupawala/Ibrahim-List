class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs] 
        ans = {}
        
        for i in strs:
            dict_key = "".join(map(str, sorted(i)))
            if dict_key not in ans: ans[dict_key] = [i]
            else: ans[dict_key].append(i)
                
        return ans.values()
    
'''
Time Complexity - O(len(n) * mlogm)
Space Complexity - O(len(n))
'''
