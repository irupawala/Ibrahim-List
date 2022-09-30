class Solution:
    def nextGreatestLetter(self, letters, target):
        start, end = 0, len(letters)-1
        
        while start <= end:
            mid = start + (end-start)//2
            if letters[mid] > target: end = mid-1
            else: start = mid+1 # key >= letters[mid]:
        
        return letters[start%len(letters)]

'''
Time Complexity - O(logN)
Space Complexity - O(1)
'''    
