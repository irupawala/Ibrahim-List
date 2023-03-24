# Uses python3


import math
import random

############################## SOLUTION FUNCTIONS ##################################################

def evalt_solution(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax_solution(i, j, ops, m, M):
    minimum = float('inf')
    maximum = -minimum

    for k in range(i, j):
        a = evalt_solution(M[i][k], M[k+1][j], ops[k])
        b = evalt_solution(M[i][k], m[k+1][j], ops[k])
        c = evalt_solution(m[i][k], M[k+1][j], ops[k])
        d = evalt_solution(m[i][k], m[k+1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return (minimum, maximum)

def get_maximum_value_solution(dataset):
    ops = dataset[1:len(dataset):2]
    ds = dataset[0:len(dataset)+1:2]
    n = len(ds)

    m = [[int(ds[i]) if i == j else 0 for i in range(n)] for j in range(n)]
    M = [[int(ds[i]) if i == j else 0 for i in range(n)] for j in range(n)]

    for i in range(1, n):
        for j in range(n-i):
            k = i + j
            m[j][k], M[j][k] = MinMax_solution(j, k, ops, m, M)

    return M[0][n-1]

##############################################################################################

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        
        
def MinAndMax(i, j, Matrix_max, Matrix_min, ops):
    minimum = math.inf
    maximum = (-math.inf)
    
    for k in range(i, j): # k divides the expression to two sub-expressions. i:k and k+1:j
#        print(f"{i}, {j}, {k}, {ops[k]}")
#        print(f"Matrix_max[{i}][{k}] = {Matrix_max[i][k]}, Matrix_max[{k+1}][{j}] = {Matrix_max[k+1][j]}")
#        print(f"Matrix_min[{i}][{k}] = {Matrix_min[i][k]}, Matrix_min[{k+1}][{j}] = {Matrix_min[k+1][j]}")
#        
        a = evalt(Matrix_max[i][k], Matrix_max[k+1][j], ops[k])
        b = evalt(Matrix_max[i][k], Matrix_min[k+1][j], ops[k])        
        c = evalt(Matrix_min[i][k], Matrix_max[k+1][j], ops[k])        
        d = evalt(Matrix_min[i][k], Matrix_min[k+1][j], ops[k])        
        
#        print(f"a = {a}, b = {b}, c = {c}, d = {d}, minimum = {minimum}, maximum = {maximum}")
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
#        print(f"minimum = {minimum}, maximum = {maximum}")

#    print(f"returned value for [{i}][{j}] = {minimum},{maximum}")
    return (minimum, maximum)
    

        

def get_maximum_value(dataset):
    
    no_of_digits = (len(dataset)//2) + 1
    ds = dataset[0:len(dataset):2]
    ops = dataset[1:len(dataset):2]
    
    Matrix_min = [[int(ds[i]) if i==j else 0 for i in range(no_of_digits)] for j in range(no_of_digits)]
    Matrix_max = [[int(ds[i]) if i==j else 0 for i in range(no_of_digits)] for j in range(no_of_digits)]
          
        
    for s in range(1, no_of_digits):
        for i in range(no_of_digits-s):
            j = i + s
            Matrix_min[i][j], Matrix_max[i][j] = MinAndMax(i, j, Matrix_max, Matrix_min, ops)
            
        
#    print("Matrix_min")
#
#    for i in range(no_of_digits):
#        for j in range(no_of_digits):
#            print(Matrix_min[i][j], end = " ")
#        print("")
#        
#    print("Matrix_max")
#            
#    for i in range(no_of_digits):
#        for j in range(no_of_digits):
#            print(Matrix_max[i][j], end = " ")
#        print("")    

    return Matrix_max[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
    
    
#    input_expression = input("Enter the expression = ")
#    ds = input_expression[0:len(input_expression):2]
#    ops = input_expression[1:len(input_expression):2]
#    get_maximum_value(input_expression)
    
    
    
##################################################### Random Tests: ##############
'''
 
    while(1):      
    

        numbers = random.randrange(0, 10, 1)
        symbol_list = ['+', '-', '*']
        n = random.randrange(0, 14, 1)
        
        ds = ""
        for i in range(n):
            num = str (random.randint(0, 9))
            symbol = random.choice(symbol_list)    
            ds = ds + num + symbol
        ds = ds + num
        
        print(ds)
           
        
        
        if (get_maximum_value(ds) == get_maximum_value_solution(ds)):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            print(f"get_maximum_value = {get_maximum_value(ds)}")
            print(f"get_maximum_value_solution = {get_maximum_value_solution(ds)}")  
            print(f"ds = {ds}")
            break       
    
'''    