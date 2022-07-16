# LintCode Link - https://www.lintcode.com/problem/178/

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    # checking if any loop in the tree
    def check_loops(self, current, previous):
        if current in self.visited: return False

        self.visited.add(current)
        for neighbor in self.adj_list[current]:
            if neighbor == previous: continue
            #if neighbor is not previous:
            if not self.check_loops(neighbor, current): return False
        return True

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n: return True
        
        
        self.adj_list = {i:[] for i in range(n)}
        # populate adj_list
        for n1, n2 in edges:
            self.adj_list[n1].append(n2)
            self.adj_list[n2].append(n1)

        self.visited = set()
        return self.check_loops(0, None) and len(self.visited) == n

'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|)
'''
