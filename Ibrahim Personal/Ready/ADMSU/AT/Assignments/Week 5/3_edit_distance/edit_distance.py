# Uses python3

import math
import random
import string

def edit_distance_solution(s, t, memo = {}):
    if len(s) == 0: return len(t)
    if len(t) == 0: return len(s)

    if (len(s), len(t)) in memo:
        return memo[(len(s), len(t))]
    delta = 1 if s[-1] != t[-1] else 0

    diag = edit_distance_solution(s[:-1], t[:-1], memo) + delta
    vert = edit_distance_solution(s[:-1], t, memo) + 1
    horz = edit_distance_solution(s, t[:-1], memo) + 1

    min_distance = min(diag, vert, horz)

    memo[(len(s), len(t))] = min_distance

    return min_distance





def edit_distance(s, t):
    #write your code here
    width = len(s) + 1
    height = len(t) + 1
    #print(f'width = {width} \nheight = {height}')
    matrix = [[ math.inf for x in range(width)] for y in range(height)]
    
    for x in range(width):
        matrix[0][x] = x
    for y in range(height):
        matrix[y][0] = y
    
   # print(matrix)
    
    for x in range(1, height) :
        for y in range(1, width) :
            if(s[y-1] == t[x-1]): 
                matrix[x][y] = min(matrix[x-1][y] + 1, matrix[x][y-1] + 1, matrix[x-1][y-1])
            else: 
                matrix[x][y] = min(matrix[x-1][y] + 1, matrix[x][y-1] + 1, matrix[x-1][y-1] + 1)    
#    print("Result Matrix")        
#    print(matrix)        
    
    return (matrix[len(t)][len(s)])
    

if __name__ == "__main__":
    #print(edit_distance(input(), input()))
  #  print(edit_distance_solution(input(), input()))
    source_string = input("Enter the source string = ")
    target_string = input("Enter the target string = ")
    
    print(edit_distance(source_string, target_string))


##################################################### Random Tests: #####################################################

'''
       
    while(1):      
    

        m1 = random.randrange(0, 4, 1)
        m2 = random.randrange(0, 4, 1)
        string1 = ''.join(random.choices(string.ascii_lowercase, k = m1)) 
        string2 = ''.join(random.choices(string.ascii_lowercase, k = m2)) 
        
        print(f'string1 = {string1}')
        print(f'string2 = {string2}')
        
        print(f'edit_distance = {edit_distance(string1, string2)}')
        print(f'edit_distance_solution = {edit_distance_solution(string1, string2)}')
        
        if (edit_distance(string1, string2) == edit_distance_solution(string1, string2)):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            break
        
'''