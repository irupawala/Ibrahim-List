# LeetCode Link - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # if the current node is a leaf and its value is equal to the targetSum, we've found a path
        if root.val == targetSum and root.left is None and root.right is None:
            return True

        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)        
        
'''
Time Complexity - O(n)
Space Complexity - O(n) # This space will be used to store the recursion stack. 
'''
