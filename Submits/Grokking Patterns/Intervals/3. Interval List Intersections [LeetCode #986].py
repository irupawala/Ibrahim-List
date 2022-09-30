# LeetCode Link - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList, secondList) :
        result = []
        i, j = 0,0
        start, end = 0, 1
        
        while i < len(firstList) and j < len(secondList):
            
            # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
            a_overlaps_b = secondList[j][start] <= firstList[i][start] and firstList[i][start] <= secondList[j][end]
            # check if intervals overlap and intervals_b[j]'s start time lies within the other intervals_a[i]
            b_overlaps_a = firstList[i][start] <= secondList[j][start] and firstList[i][end] >= secondList[j][start] 
             
            # store the the intersection part
            if a_overlaps_b or b_overlaps_a:
                result.append([max(firstList[i][start], secondList[j][start]), min(firstList[i][end], secondList[j][end])])
            
            # move next from the interval which is finishing first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result    
                               
'''
Time Complexity - O(M+N)
Space Complexity - O(1)
'''        
