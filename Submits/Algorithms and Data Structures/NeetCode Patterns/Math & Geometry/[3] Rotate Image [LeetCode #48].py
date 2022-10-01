class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        
        while left < right: 
            top, bottom = left, right
            for i in range(right-left):
                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]           
                matrix[top+i][right] = topLeft
            
            left += 1
            right -= 1
            

            
#S = Solution()
#print(S.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

'''
Time Complexity - O(n+m)
Space Complexity - O(1)
'''

