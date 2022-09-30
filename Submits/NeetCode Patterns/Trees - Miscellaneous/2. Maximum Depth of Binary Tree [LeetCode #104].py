# LeetCode Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        qmain = deque()
        max_depth = 0
        qmain.append(root)
        
        while qmain:   
            for i in range(len(qmain)):
                node = qmain.popleft()
                if node.left: qmain.append(node.left)
                if node.right: qmain.append(node.right)
            max_depth += 1
        return max_depth
            
'''
Time Complexity - O(n)
Space Complexity - O(n) to store in the queue
'''            
