# LeetCode Link - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
  
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        queue = deque()
        queue.append(root)
        while queue:
            previousNode = None
            levelSize = len(queue)
            # connect all nodes of this level
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if previousNode:
                    previousNode.next = currentNode
                previousNode = currentNode

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)      
        
        return root
    
'''
Time Complexity - O(N)
Space Complexity - O(N)
'''
