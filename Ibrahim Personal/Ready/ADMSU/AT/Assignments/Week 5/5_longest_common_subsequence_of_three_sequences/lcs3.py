#Uses python3

#import sys
import random


def lcs3(a, b, c):
    #write your code here
    width = len(a) + 1
    height = len(b) + 1
    depth = len(c) + 1
#    print(f'width = {width} \nheight = {height} \ndepth = {depth}')

    matrix = [[[0 for d in range(depth)] for w in range(width)] for h in range(height)]

#   First number represents row, second column and third depth
#    print (matrix)
#    matrix[1][1][2] = 20 

    for d in range(1, depth) :
        for w in range(1, width) :
            for h in range(1, height) :
                    
                if ((a[w-1] == b[h-1]) and (b[h-1] == c[d-1])) :
                    matrix[h][w][d] = matrix[h-1][w-1][d-1] + 1
                    #print(f'true (a[{w-1}] : {a[w-1]}, b[{h-1}]:{b[h-1]}, c[{d-1}] : {c[d-1]}) = matrix[{h}][{w}][{d}] = {matrix[h][w][d]}')
                else:
                    max_value = max(matrix[h-1][w][d], matrix[h][w-1][d], matrix[h-1][w-1][d], matrix[h][w][d-1], matrix[h][w-1][d-1], matrix[h-1][w][d-1])
                    matrix[h][w][d] = max_value 
                    #print(f'NOT true = matrix[{h}][{w}][{d}] = {matrix[h][w][d]}')                      
                    
#    print("\nOutput Matrix \n")        
#    for d in range(0, depth) :
#        print (f"depth = {d}")
#        for h in range(0, height):
#            for w in range(0, width) :    
#                print (matrix[h][w][d], end =" ")
#            print("")              

#    print("\n Detailed Output Matrix \n")        
#    for d in range(1, depth) :
#        print (f"depth = {d}")
#        for h in range(1, height):
#            for w in range(1, width) :    
#                print (f'matrix[{h}][{w}][{d}] = {matrix[h][w][d]}', end =" ")
#            print("")
    
#    return matrix
#    print(f'a = {len(a)} b = {len(b)} c = {len(c)}')
    return matrix[len(b)][len(a)][len(c)] 


def lcs3_solution(a, b, c):
    lena = len(a); lenb = len(b); lenc = len(c)
    dp = [[[0 for _ in range(lenc+1)] for _ in range(lenb+1)] for _ in range(lena+1)]

    for i in range(lena+1):
        for j in range(lenb+1):
            for k in range(lenc+1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                else:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1] if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1] else max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[-1][-1][-1]


if __name__ == '__main__':
    
    data = list(map(int, input("Enter the complete sequence lcs3 = ").split()))
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    
    print(lcs3(a, b, c))
    
#    lcs3(a, b, c)
    
    
 
'''

##################################################### Random Tests: ##############

    while(1):      
    

        an = random.randrange(0, 100, 1)
        bn = random.randrange(0, 100, 1)
        cn = random.randrange(0, 100, 1)
        
        a = [random.randrange(0, 1000, 1) for i in range(an)]
        b = [random.randrange(0, 1000, 1) for i in range(bn)]
        c = [random.randrange(0, 1000, 1) for i in range(cn)]
        
        print(f'a = {a}')
        print(f'b = {b}')
        print(f'c = {c}')
        
        print(f'lcs3 = {lcs3(a, b, c)}')
        print(f'lcs3_solution = {lcs3_solution(a, b, c)}')
        
        if (lcs3(a, b, c) == lcs3_solution(a, b, c)):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            break    
    
##################################################### Sample Inputs: ##############  


#Sample Inputs
#
#5 8 3 2 1 7 7 8 2 1 3 8 10 7 6 6 8 3 1 4 7 
#3 1 2 3 3 2 1 3 3 1 3 5

'''
