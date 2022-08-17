from collections import deque

class Solution:
    def permute(self, nums):
        numsLength = len(nums)
        result = []
        permutations = deque()
        permutations.append([])
        for currentNumber in nums:
            # we will take all existing permutations and add the current number to create new permutations
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()
                # create a new permutation by adding the current number at every position
                for j in range(len(oldPermutation)+1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)

        return result
'''  
S = Solution()
print(S.permute([1,2,3]))
'''  


'''
Time Complexity - O(N*N!)
Space Complexity - O(N*N!)
'''
