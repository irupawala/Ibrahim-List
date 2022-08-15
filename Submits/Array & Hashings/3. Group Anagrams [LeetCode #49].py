'''
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

'''
Time Complexity - O(len(strs) * mlogm)
Space Complexity - O(len(strs))
'''


# Linear time algorithm by Neetcode

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


'''
Time Complexity - O(len(str) * m * 26)
Space Complexity - O(len(str) * m)
'''
