# Uses python3
import sys
#import random

def optimal_weight(Weight, weight_items):
    # write your code here
#    result = 0
#    for x in w:
#        if result + x <= W:
#            result = result + x
#    return result
    
    width = Weight + 1
    n = len(weight_items) + 1
    
    value = [[0 for _ in range(width)] for _ in range(n)]
    
#    print(value)
    
    for i in range(1, n):
        for j in range(1, width):
            value[i][j] = value[i-1][j] # Copy the value of previous row in this row for the same column
            
            if (weight_items[i-1] <= j): # Here as weight and value are same if weight is less then j
                val = value[i-1][j-weight_items[i-1]] + weight_items[i-1] # copy val as value[i-1][w-wi] + vi # REPEAT NOT ALLOWED
#                val = value[i][j-weight_items[i-1]] + weight_items[i-1] # copy val as value[i-1][w-wi] + vi # REPEAT ALLOWED
                
                if (value[i][j] < val):
                    value[i][j] = val
            
    
#    print("Result Matrix")
#    for i in range(0, n):
#        print("[", end = " ")
#        for j in range(0, width):
#            print (value[i][j], end = " ")
#        print("]", end = " ")
#        print("")
                          
#    return value[n-1][width-1]    
    return value[-1][-1]
        
def optimal_weight_solution(W, w):

    res = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]

    for i in range(1, len(res)):
        for j in range(1, len(res[i])):
            res[i][j] = res[i-1][j]
            if w[i-1] > j:
                continue
            x = res[i-1][j - w[i-1]] + w[i-1]
            if x > res[i][j]:
                res[i][j] = x

    return res[-1][-1]        

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
#    W, n, *w = list(map(int, input("Enter the input: " ).split()))
    print(optimal_weight(W, w))
#    
##    optimal_weight(W, w)
#    
    
    
##################################################### Random Tests: ##############
'''
 
    while(1):      
    

        W = random.randrange(0, 10000, 1)
        n = random.randrange(0, 300, 1)

        
        
        print(f'W = {W}')
        print(f'n = {n}')
        
        w = []
        for i in range(n):
            k = random.randint(1, 100000)
            w.append(k)     
            
        print('w = ')
        for x in w:
            print(x, end=' ')
        print('\n')                
        
        
        if (optimal_weight(W, w) == optimal_weight_solution(W, w)):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            print(f"optimal_weight = {optimal_weight(W, w)}")
            print(f"optimal_weight_solution = {optimal_weight_solution(W, w)}")            
            break       
'''
    
##################################################### Sample Inputs: ##############  


#Sample Inputs
#
# 10 3 1 4 8 
# 5 2 1 4
            
        
# 7 3 6 13 4