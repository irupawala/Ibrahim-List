# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(current_node):
            if not current_node:
                return False
            
            # Left Recursion
            left = dfs(current_node.left)
            
            # Right Recursion
            right = dfs(current_node.right)
            
            # If the current_node is one of p or q
            mid = current_node == p or current_node == q
            
            # If any two of the three flags left, right or mid become True.
            if mid + left + right == 2:
                self.ans = current_node
                

            # Return True if either of the three bool values is True.
            return mid or left or right            
        
        
        # Traverse the tree
        dfs(root)
        return self.ans        
    
'''
Time Complexity - O(n)
Space Complexity - O(n)
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q = p, q
        
        def inorderTraversal(root):
            if not root: return None 
            if root.val == self.p.val or root.val == self.q.val: return root
            
            left = inorderTraversal(root.left)
            right = inorderTraversal(root.right)

            if left and right: return root
            return left if left != None else right
        
        return inorderTraversal(root)
    
