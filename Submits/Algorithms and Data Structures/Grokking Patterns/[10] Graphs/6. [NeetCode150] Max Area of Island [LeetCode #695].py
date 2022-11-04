# LeetCode Link - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.columns = len(grid), len(grid[0])
        self.visited = set()
        self.max_area = 0
        
        def dfs(r, c):
            if (r,c) in self.visited or r < 0 or r == self.rows or c < 0 or c == self.columns or grid[r][c] == 0:
                return 
            
            self.counter += 1
            self.visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)            
            return 
            
        for r in range(self.rows):
            for c in range(self.columns):
                if (r,c) not in self.visited and grid[r][c] == 1:
                    self.counter = 0
                    dfs(r, c)
                    self.max_area = max(self.max_area, self.counter)
                    
        return self.max_area
                
'''
Time Complexity - O(n.m)
Space Complexity - O(n.m.4^(n.m)) for the recursion stack
'''        
