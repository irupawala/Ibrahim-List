# LeetCode Premium - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# LintCode Link - LintCode Premium

from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        # write your code here

        result_list = []
        visited = {i.label:False for i in nodes}

        def dfs(i, connected_list):

            visited[i.label] = True
            connected_list.append(i.label)

            for j in i.neighbors:
                if not visited[j.label]:
                    dfs(j, connected_list)

            i.neighbors = [] # This line is super-critical to reduce time Complexity
            return connected_list

        for i in nodes:
            if not visited[i.label]:
                result = sorted(dfs(i, []))
                if result: result_list.append(result)

        return result_list

    
                
'''
Time Complexity - O(|V|+|E|)
Space Complexrity - O(|V|)
'''
