# LeetCode Link - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.count_paths_recursive(root, targetSum, [])


    def count_paths_recursive(self,currentNode, S, currentPath):
        if currentNode is None:
            return 0

        # add the current node to the path
        currentPath.append(currentNode.val)
        pathCount, pathSum = 0, 0
        # find the sums of all sub-paths in the current path list
        for i in range(len(currentPath)-1, -1, -1):
            pathSum += currentPath[i]
             # if the sum of any sub-path is equal to 'S' we increment our path count.
            if pathSum == S:
                pathCount += 1

        # traverse the left sub-tree
        pathCount += self.count_paths_recursive(currentNode.left, S, currentPath)
        # traverse the right sub-tree
        pathCount += self.count_paths_recursive(currentNode.right, S, currentPath)

        # remove the current node from the path to backtrack
        # we need to remove the current node while we are going up the recursive call stack
        del currentPath[-1]

        return pathCount        
    
'''
Time Complexity - O(N^2) in the worst case,  This is due to the fact that we traverse each node once, but for every node, we iterate the current path. The current path, in the worst case, can be O(N) (in the case of a skewed tree). But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). So the best case of our algorithm will be O(NlogN)
Space Complexity - O(N) - Worst Case when tree is a linkedlist for Recursion stack
'''
