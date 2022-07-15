# LeetCode Link - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Nod
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy # Notice that Class object is used as a key in the Dictionary, It also works with node.val
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None


'''    
if __name__ == "__main__":
    inputDict = {}
    node_0 = Node(0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    inputDict[0] = node_0
    inputDict[1] = node_1
    inputDict[2] = node_2
    inputDict[3] = node_3

    node_0.neighbors.append(node_1)
    node_0.neighbors.append(node_3)

    node_1.neighbors.append(node_0)
    node_1.neighbors.append(node_2)

    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)

    node_3.neighbors.append(node_0)
    node_3.neighbors.append(node_2)

    S = Solution()
    S.cloneGraph(node_0)
'''
        
'''
Time Complexity - O(|E|+|V|)
Space Complexity - O(|E|+|V|)
'''
