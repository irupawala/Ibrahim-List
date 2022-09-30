class Solution:
    def isValidSudoku(self, board):
        
        # Check row:
        for row in board:
            row_set = set()
            for no in row:
                if no != ".":
                    if int(no) not in range(1, 10) or no in row_set: return False
                    else: row_set.add(no)
                    
        # Check column:
        for column in range(len(board[0])):
            column_set = set()
            for row in range(len(board)):
                no = board[row][column]
                if no != ".":
                    if int(no) not in range(1, 10) or no in column_set: return False
                    else: column_set.add(no)
                    
        # Check box:
        for column_no in [0,3,6]:
            for row_no in [0,3,6]:
                box_set = set()
                for row_offset in [0,1,2]:
                    for column_offset in [0,1,2]:
                        no = board[row_no+row_offset][column_no+column_offset]
                        if no != ".":
                            if int(no) not in range(1, 10) or no in box_set: return False
                            else: box_set.add(no)
                                
        return True

# NeetCode Solution 
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
'''
    
'''
S = Solution()
print(S.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
'''

                        
