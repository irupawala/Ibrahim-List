# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both the trees are empty
            return True
        
        if (not p and q) or (p and not q) or p.val != q.val: # Checking values of current node
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
