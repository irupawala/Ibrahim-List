class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows, self.columns = len(board), len(board[0])
        self.visited = set()
        output = board[:]
        
        def dfs(r,c):
            if (r == 0 or r == self.rows-1 or c == 0 or c == self.columns-1) and board[r][c] == "O" : self.validisland = False
            
            if r == 0 or r == self.rows-1 or c == 0 or c == self.columns-1 or (r,c) in self.visited or board[r][c] == "X":
                return 
            
            self.toBeFlipped.add((r,c))
            self.visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c) 
            dfs(r,c-1) 
            dfs(r,c+1)
            
        
        
        for r in range(1, self.rows-1):
            for c in range(1, self.columns-1):      
                if (r,c) not in self.visited and board[r][c] == "O":
                    self.toBeFlipped = set()
                    self.validisland = True
                    dfs(r,c)
                    if self.validisland:
                        for i, j in self.toBeFlipped:
                            output[i][j] = "X"
                
                                     
        return output

# NeetCode Solution
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)
        
        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"                 
'''    
      
'''
Time Complexity - O(n.m.4^(n.m)) 
Space Complexity - O(n.m)for the recursion stack
'''      
