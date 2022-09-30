# LeetCode Link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        result = []
        def InOrderTraversal(root):
            if not root: return 
            InOrderTraversal(root.left)
            result.append(root.val)
            InOrderTraversal(root.right)
            
        InOrderTraversal(root)
        return(result[k-1])
'''

# Iterative Solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            
'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
