# LeetCode Link - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.find_root_to_leaf_path_numbers(root, 0)


    def find_root_to_leaf_path_numbers(self,currentNode, pathSum):
        if currentNode is None:
            return 0

        # calculate the path number of the current node
        pathSum = 10 * pathSum + currentNode.val

        # if the current node is a leaf, return the current path sum
        if currentNode.left is None and currentNode.right is None:
            return pathSum

        # traverse the left and the right sub-tree
        return self.find_root_to_leaf_path_numbers(currentNode.left, pathSum) + self.find_root_to_leaf_path_numbers(currentNode.right, pathSum)
        
'''
Time Complexity - O(N)
Space Complexity - O(N)
'''
