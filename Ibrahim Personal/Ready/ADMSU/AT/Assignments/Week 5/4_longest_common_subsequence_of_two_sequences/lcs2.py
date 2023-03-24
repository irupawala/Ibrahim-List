#Uses python3

import sys
#import math

def lcs2(a, b):
    #write your code here
    width = len(a) + 1
    height = len(b) + 1
    matrix = [[0 for w in range(width)] for h in range(height)] 

    for y in range(1, width) :
        for x in range(1, height) :

            if (b[x-1] == a[y-1]) :  # If the value is equal then increment the diagonal value of matrix
                    matrix[x][y] = matrix[x-1][y-1] + 1
            else:
                max_value = max(matrix[x-1][y], matrix[x][y-1]) # If the value is different then take the same value as sides
                matrix[x][y] = max_value         
                
    return (matrix[len(b)][len(a)])

if __name__ == '__main__':
    
#    data = list(map(int, input("Enter the complete sequence lcs2 = ").split()))

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]
    
    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    
    print(lcs2(a, b))

'''
Sample Inputs

3 2 7 5 2 2 5
5 8 3 2 1 7 7 8 2 1 3 8 10 7
4 2 7 8 3 4 5 2 8 7
5 2 7 7 7 5 4 2 7 7 5
7 8 2 1 3 8 10 7 5 8 3 2 1 7 7
4 2 7 8 3 4 5 2 8 7
3 3 3 1 3 1 3 3 


'''