# Uses python3
import sys
import math

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def minOperations(n) :
    
    table_dp =   [-1] * (n+1)
    seq = [n]  

    for number, min_operations in enumerate((table_dp)):
        
        min1 = min2 = min3 = math.inf
        #min2 = math.inf
        #min3 = math.inf
        
        # Creating table_dp with minimum no of operations required for all numbers from 0 to n
        if (number == 0 or number == 1):
            table_dp[number] = 0
            continue
            
        if (number % 3 == 0):
            min3 = table_dp[number // 3]
            
        if (number % 2 == 0):
            min2 = table_dp[number // 2]
        
        min1 = table_dp[number-1]
        minimum = min(min1, min2, min3)
        table_dp[number] = minimum + 1
        
        #table_dp[number] = min(min1, min2, min3) + 1
        # table_dp[number] = min(table_dp[number-1], min2, min3) + 1
    
    
        
    while (n != 1) :
        
        # After creating a table of min number of operations we have to create a sequence which the algorithm has followed to get to that minimum no of operations required for that number
        # Creating a two dimensional matrix with first column as number and second column as corresponding min_operations
        matrix =   [[math.inf, math.inf]] * (3)

        if (n % 3 == 0):
            matrix[2] = [(n // 3), table_dp[n // 3]]   # first column as no and second their minimum_ops
            
        if (n % 2 == 0):
            matrix[1] = [(n // 2), table_dp[n // 2]]
                
        matrix[0] = [(n - 1), table_dp[n - 1]]    

        
        # finding the previous n which has min operations from 3 possibilities n/3, n/2 and n-1
        n = min(matrix, key = lambda t: t[1])[0] # comparing the second column (min_ops) from 3 rows and passing off the number (first column) in the sequence
        seq.append(n)
    
    return seq



if __name__ == '__main__':
    
    #input = sys.stdin.read()
    #n = int(input)
    n = int(input("Enter the number = "))
    #sequence = list(optimal_sequence(n))
    
    sequence = list(minOperations(n))
    print(len(sequence) - 1)
    for x in reversed(sequence):
        print(x, end=' ')
