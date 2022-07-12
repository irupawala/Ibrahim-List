from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        result = []
        
        q.append(root)
        
        while q:            
            level_nodes = []
            len_q = len(q)
            for i in range(len_q):
                _node = q.popleft()
                if _node:
                    level_nodes.append(_node.val)
                    q.append(_node.left)
                    q.append(_node.right)
            if level_nodes: result.append(level_nodes)
        
        return result

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
            
        
