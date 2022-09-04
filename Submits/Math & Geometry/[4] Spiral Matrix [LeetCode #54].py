class Solution:
    def spiralOrder(self, matrix):
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        result = []
        
        l, r = 0, COLUMNS
        top, bottom = 0, ROWS
        total_count = ROWS * COLUMNS
        
        while l < r and top < bottom:
            
            for i in range(l, r-1):
                result.append(matrix[top][i])
                
            for i in range(top, bottom):
                result.append(matrix[i][r-1])
                
            if len(result) == total_count: return result
                
            for i in range(r-2, l-1, -1):
                result.append(matrix[bottom-1][i])
                
            for i in range(bottom-2, top, -1):
                result.append(matrix[i][l])
                
            r -= 1
            l += 1
            bottom -= 1
            top += 1
        
        return result
                
                
'''              
S = Solution()
print(S.spiralOrder([[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24], [25,26,27,28,29,30]]))
'''  

'''
Time Complexity - O(n+m)
Space Complexity - O(1)
'''
