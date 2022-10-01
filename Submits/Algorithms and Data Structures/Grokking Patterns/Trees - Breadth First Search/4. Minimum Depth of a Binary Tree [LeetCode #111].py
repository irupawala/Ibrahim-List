# LeetCode Link - https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        minimumTreeDepth = 0
        
        while q:    
            minimumTreeDepth += 1
            len_q = len(q)
            for i in range(len_q):
                _node = q.popleft()
                if not _node.left and not _node.right: return minimumTreeDepth
                if _node.left:
                    q.append(_node.left)
                if _node.right:
                    q.append(_node.right)

        return result

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
                    
