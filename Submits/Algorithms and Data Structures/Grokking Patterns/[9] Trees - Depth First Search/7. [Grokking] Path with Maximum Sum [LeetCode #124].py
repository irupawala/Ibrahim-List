# LeetCode Link - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.globalMaxSum = float("-inf")
        
        def path_sum(root):
            if not root: return 0
            
            sum_l, sum_r = path_sum(root.left), path_sum(root.right)

            # ignore paths with negative sums, since we need to find the maximum sum we should
            # ignore any path which has an overall negative sum.            
            sum_l, sum_r = max(sum_l, 0), max(sum_r, 0)

            # maximum path sum at the current node will be equal to the sum from the left subtree +
            # the sum from right subtree + val of current node            
            localMaxSum = sum_l + sum_r + root.val

            # update the global maximum sum
            self.globalMaxSum = max(self.globalMaxSum, localMaxSum)

            # maximum sum of any path from the current node will be equal to the maximum of
            # the sums from left or right subtrees plus the value of the current node
            return max((root.val+sum_l), (root.val+sum_r))
        
        path_sum(root)
        return self.globalMaxSum
        
'''
Time Complexity - O(N)
Space Complexity - O(N) # This space will be used to store the recursion stack
'''
