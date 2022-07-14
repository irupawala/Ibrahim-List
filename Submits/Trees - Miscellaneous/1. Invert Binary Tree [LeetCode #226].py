# LeetCode Link - https://leetcode.com/problems/invert-binary-tree/

# DFS NeetCode Solution 

from collections import deque

# Definition for a binary tree node.
#class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
'''
Time Complexity - O(N)
Space Complexity - O(1)
'''

## BFS Solution

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None 
        
        q = deque()
        q.append(root)
        
        while q:
            len_q = len(q)
            for i in range(len_q):  
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)                    
                    saved_node = node.left
                    node.left = node.right
                    node.right = saved_node

                    
        return root

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
