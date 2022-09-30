class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtracking(subset, pos, total):
            if total == 0:
                result.append(subset.copy())
            if pos >= len(candidates) or total < 0:
                return 
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                backtracking(subset, i+1, total-candidates[i])
                subset.pop()
                total+candidates[i]
                prev = candidates[i]

        backtracking([], 0, target)
        return result
    
#S = Solution()
#print(S.combinationSum2([10,1,2,7,6,1,5], 8))

'''
Time Complexity - O(2**N), N = No of candidates
Space Complexity - O(N) for the recursion stacks
'''
