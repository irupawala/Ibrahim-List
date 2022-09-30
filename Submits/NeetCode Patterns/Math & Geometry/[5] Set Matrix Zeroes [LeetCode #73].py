class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        zero_locations = []
        
        # find zero_locations
        for i in range(ROWS):
            for j in range(COLUMNS):
                if matrix[i][j] == 0: zero_locations.append((i,j))

        for (x,y) in zero_locations:
            # Making ROWS 0
            for i in range(ROWS):
                matrix[i][y] = 0
            # Making COLUMNS 0
            for j in range(COLUMNS):
                matrix[x][j] = 0
                
'''
Time Complexity - O(n*m) # when all entries are 0
Space Complexity - O(len of zero_locations)
'''
        
