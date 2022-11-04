# LeetCode Link - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        dp = dict()
        self.longest_path = 0
        
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        
        def dfs(i,j, path_len):
            if (i,j) in dp: return path_len + dp[(i,j)] 
            path_left, path_right, path_top, path_bottom = path_len, path_len, path_len, path_len
            
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]: # left
                path_left = dfs(i, j-1, path_len) 
            if j+1 <= COLUMNS-1 and matrix[i][j+1] > matrix[i][j]: # right 
                path_right = dfs(i, j+1, path_len)   
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]: 
                path_top = dfs(i-1, j, path_len) # top    
            if i+1 <= ROWS-1 and matrix[i+1][j] > matrix[i][j]: 
                path_bottom = dfs(i+1, j, path_len) # bottom
            
                
            dp[(i,j)] = max(path_left, path_right, path_top, path_bottom) + 1
            self.longest_path = max(self.longest_path, dp[(i,j)])
            
            return dp[(i,j)]  #backtracking
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                if (i,j) in dp: self.longest_path = max(self.longest_path, dp[(i,j)])
                else: dfs(i,j, 0)
                    
        return self.longest_path
                
'''
Time Complexity - O(m.n)
Space Complexity - O(m.n)
'''


# NeetCode Solution


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
