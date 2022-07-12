LeetCode Link - https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.treeDiameter = 0
        return self.find_diameter(root)

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        # if the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        #if leftTreeHeight != 0 and rightTreeHeight != 0:

        # diameter at the current node will be equal to the height of left subtree +
        # the height of right sub-trees + '1' for the current node
        diameter = leftTreeHeight + rightTreeHeight 

        # update the global tree diameter
        self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1        

'''
Time Complexity - O(N)
Space Complexity - O(N)
'''
