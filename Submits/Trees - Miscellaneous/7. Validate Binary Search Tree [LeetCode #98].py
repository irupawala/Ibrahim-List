# LeetCode Link - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def InOrderTraversal(root, min_value, max_value):
            if not root: return True
            if root.val <= min_value or root.val >= max_value: return False
            return InOrderTraversal(root.left, min_value, root.val) and InOrderTraversal(root.right, root.val, max_value)
        
        return InOrderTraversal(root, float("-inf"), float("inf"))
    
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
