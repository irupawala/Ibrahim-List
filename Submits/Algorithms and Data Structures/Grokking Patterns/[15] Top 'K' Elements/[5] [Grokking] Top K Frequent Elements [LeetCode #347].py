# Leetcode Link - https://leetcode.com/problems/top-k-frequent-elements/

'''
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        ans = []
        heap = []
        
        for num in set_nums: 
            heappush(heap, [-nums.count(num), num])
            
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans

'''

'''
Time Complexity - O(unique_nums*log(unique_nums) + O(k*log(unique_nums))
Space Complexity - O(unique_nums)
'''

'''
# NeetCode Linear time solution
'''
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
S = Solution()
print(S.topKFrequent([1,1,1,2,2,3], 2))
'''
Time Complexity - O(n) + O(n) + O(k) =~ O(n)
Space Complexity - O(n)
'''        
