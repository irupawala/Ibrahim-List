# LeetCode Link - https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    # numTree[4] = numTree[0] * numTree[3] + # root 1
    #              numTree[1] * numTree[2] + # root 2
    #              numTree[2] * numTree[1] + # root 3
    #              numTree[3] * numTree[0] # root 4
                
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n+1)
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
                # print(nodes, root, left, right, total)
            numTree[nodes] = total
            
        # print(numTree)
        return numTree[n] 
    
'''
Time Complexity - O(n**2) because for calculating for any n we have to calculate for all n-1
Space Complexity - O(n)
'''


'''
class Solution:
    def __init__(self):
        self.cache = {}
    def numTrees(self, n: int) -> int:
        if n in self.cache: return self.cache[n]
        if n <= 1:
            return 1
        count = 0
        for i in range(1, n+1):
            # making 'i' root of the tree
            countOfLeftSubtrees = self.numTrees(i - 1)
            countOfRightSubtrees = self.numTrees(n - i)
            count += (countOfLeftSubtrees * countOfRightSubtrees)

        self.cache[n] = count
        return count
'''

'''
Time Complexity - O(n**2) because for calculating for any n we have to calculate for all n-1
Space Complexity - O(n) for the cache
'''