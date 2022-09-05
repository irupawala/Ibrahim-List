class Solution:
    def flipAndInvertImage(self, image):
        C = len(image)
        for row in image:
            for i in range((C+1)//2):
                row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1

        return image        
    
'''
Time Complexity - O(n) as we iterate through all elements of the input
Space Complexity - O(1)
'''
