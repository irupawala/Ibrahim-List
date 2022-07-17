# LeetCode Link - https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        
        visited = set()
        rows, columns = len(grid), len(grid[0])
        result, rotten_oranges, total_oranges, counter = 0, 0, 0, 0
        q = deque()
        
        # Count all oranges because we need to return only when all oranges gets rotten
        for k in grid:
            total_oranges = total_oranges + k.count(1) + k.count(2)
        
        # Add all rotten oranges to the queue
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append((r,c))
                    counter = -1
                    
        # If all fresh oranges are to turn rotten then all fresh oranges will be added to queue
        while q:
            counter += 1
            queue_len = len(q)

            for _ in range(queue_len):
                rotten_oranges += 1
                x,y = q.popleft()
                visited.add((x,y))

                neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for i, j in neighbors:
                    if i in range(0,rows) and j in range(0,columns) \
                    and (i,j) not in visited and grid[i][j] == 1 and (i,j) not in q:
                        q.append((i,j))
                result = max(result, counter)                         
        
        return result if rotten_oranges == total_oranges else -1

'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|)
'''
