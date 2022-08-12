class Solution:
    def searchMatrix(self, matrix, target) :
        concat_list = [j for i in matrix for j in i]
        return self.binary_search(concat_list, target)
    
    def binary_search(self, arr, target):
        start, end = 0, len(arr)-1
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == target: return True
            elif arr[mid] > target: end = mid-1
            else: start = mid+1
        
        return False

'''
Time Complexity - O(N.M) + O(log(N+M))
Space Complexity - O(N.M)
'''

# NeetCode Solution 
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
    
'''

'''
Time Complexity - O(logN) + O(logM)
Space Complexity - O(1)
'''
