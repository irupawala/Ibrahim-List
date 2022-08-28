class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def find_unique_trees(self, n: int) -> int:
        if n <= 0:
            return []
        return len(self.findUnique_trees_recursive(1, n))       

    def findUnique_trees_recursive(self, start, end):
        result = []
        # base condition, return 'None' for an empty sub-tree
        # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
        # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
        # both of these should return 'None' for the left and the right child
        if start > end:
            result.append(None)
            return result

        for i in range(start, end+1):
            # making 'i' the root of the tree
            leftSubtrees = self.findUnique_trees_recursive(start, i - 1)
            rightSubtrees = self.findUnique_trees_recursive(i + 1, end)
            for leftTree in leftSubtrees:
                for rightTree in rightSubtrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    result.append(root)

        return result
        
'''
Time Complexity - O(n*2^n)
Space Complexity - O(2^n)
'''
