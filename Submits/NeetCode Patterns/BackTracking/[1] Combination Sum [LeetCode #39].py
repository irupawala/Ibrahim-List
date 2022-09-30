class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def dfs(target, subset, i):
            if target == 0:
                result.append(subset.copy())
                return 
            
            if target < 0 or i >= len(candidates): 
                return 
            
            subset.append(candidates[i])
            dfs(target-candidates[i], subset, i) # include a no

            subset.pop()
            dfs(target, subset, i+1) # Do not include a no
        
        dfs(target, [], 0)
        
        return result
    
#S = Solution()
#print(S.combinationSum([2,3,6,7], 7))

'''
Time Complexity - O(2**T), where T is target, note that it's not N as recursion does not stops untill it reaches T
Space Complexity - O(T), Recursion stack could take same elements as long as Target is reached
'''
