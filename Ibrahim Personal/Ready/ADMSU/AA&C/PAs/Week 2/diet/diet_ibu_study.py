# python 3

import copy
import math
VeryBigNumber = 1e9

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    size = len(used_rows)
    pivot_element = Position(0, 0)
    
    for pivot_column in range(size):
        for pivot_row in range(size):
            if ((used_rows[pivot_row] == False) and (used_columns[pivot_column] == False) and a[pivot_row][pivot_column]):
                pivot_element.row = pivot_row
                pivot_element.column = pivot_column
                return pivot_element
    
    return 0
    
def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    size = len(b)
    
    pivot_element_divisor = a[pivot_element.row][pivot_element.column]
    for pivot_column_index in range(size):
        a[pivot_element.row][pivot_column_index] = a[pivot_element.row][pivot_column_index] / pivot_element_divisor
    b[pivot_element.row] = b[pivot_element.row] / pivot_element_divisor
    
    for row_index in range(size):
        if row_index != pivot_element.row:
            subract_divisor = a[row_index][pivot_element.column]   
            for column_index in range(size):
                a[row_index][column_index] = a[row_index][column_index] - a[pivot_element.row][column_index] * subract_divisor                
            b[row_index] =  b[row_index] - b[pivot_element.row] * subract_divisor


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        
        if pivot_element == 0:
#            return True, b
            return b
        
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

#    return True, b
    return b

def addEquations( n, mm, A, b, Big_number ):
    for i in range(mm): # For adding another 3 ineqaulities belonging to varaibles >= 0 
        e = [0.0] * mm
        e[i] = -1.0
        A.append(e)
        b.append(0.0)
    # For adding the inequality a1 + a2 + a3 < 1e9 for checking the case of infinite solutions        
    A.append([1.0] * mm)
    b.append(Big_number)
    print(f"A={A}")
    print(f"b={b}")
    
def PowerSet(set):

    set_size = len(set)
    pow_set_size = (int) (math.pow(2, set_size)) # set_size of power set of a set with set_size n is (2**n -1)
    power_set = []
     
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size): # Inner loop (1<<j) always produces 1,2,4... binary and with 1,2,3,4... produces binary representation of 1,2,4.. 
        subset = [] # for adding the elements contained in subset 
        for j in range(0, set_size):
            if((counter & (1 << j)) > 0):  # Check if jth bit in the counter is set If set then print jth element from set        
                subset.append(set[j])
        power_set.append(subset) 
    return power_set 
    

def checkResult( n, mm, A, b, c, result, lastEquation, ans, bestScore ):
    
    # Checking inequalities (a1, a2,..., amm) > 0 for each variable in result , that is not smaller then -0.001
    for r in result:
        if r < -1e-3:
            print(f"r={r}")
            return False, ans, bestScore
        
    # Checking if the solution results obained (a1, a2,..., amm) satisfies all inequalities in n   
    for i in range(n):
        r = 0.0
        for j in range(mm):
            print(f"A[i][j] = {A[i][j]}")
            print(f"result[j] = {result[j]}")
            print(f"A[i][j] * result[j] = {A[i][j] * result[j]}")
            print(f"r = {r}")
            r += A[i][j] * result[j]
            print(f"post_r = {r}")
        print(f"b[i] = {b[i]}")    
        
        # if r is greater then b by 0.001 meaning ineqaulity does not hold true
        if r > b[i] + 1e-3:
            return False, ans, bestScore # isAccepted, ans, bestScore
        
    # After checking all inequalities calibrating scores    
    score = 0.0   
    for j in range(mm):
        score += c[j] * result[j]
    print(f"score={score}")    
        
    # if score is less than bestScore then the result is not accpeted  
    if score <= bestScore:
        return False, ans, bestScore
    
    else:
        if lastEquation: # If lastEquation is true this means that equation a1+a2+.. <= 10^9 is involved and hence one variable is <= 10^9
            return True, 1, score
        else:
            return True, 0, score

def solve_diet_problem( n, mm, A, b, c, Big_number=VeryBigNumber ):
    addEquations(n, mm, A, b, Big_number)
    l = n + mm + 1 # total inequalitiles are n plus m>1 plus 1 for infinitely many solutions
    ans = -1
    bestScore = -float('inf')
    bestResult = None
    inequalities_no = [i for i in range(l)]
    power_set = PowerSet(inequalities_no)
    for x in range(2 ** l): # There are total 2^l subsets of the list of l inequalities
#        usedIndex = [i for i in range(l) if ((x / 2 ** i) % 2) // 1 == 1] # Very fine and advanced method of generating powerset see power_set_bessie.py to understand
        usedIndex = power_set[x]
        print(" ")
        print(f"x={x}")
        print(f"usedIndex={usedIndex}")
        if len(usedIndex) != mm:
            continue
        lastEquation = False
        print(f"usedIndex_length={usedIndex}")
        print(f"A={A}")
        print(f"b={b}")       
        if usedIndex[-1] == l - 1:
            lastEquation = True # here last equation is the equation which has inequality a1+a2+... < 10^9. The equations list A is created such that A is the last equation
            print(f"lastEquation = {lastEquation}")
        As = [A[i] for i in usedIndex]        
        bs = [b[i] for i in usedIndex]
        print(f"As={As}, bs={bs}")
#        solved, result = SolveEquation(copy.deepcopy(Equation(As, bs)))
        result = SolveEquation(copy.deepcopy(Equation(As, bs)))
#        print(f"solved={solved}, result={result}")
        print(f"result={result}")
#        if solved:
        isAccepted, ans, bestScore = checkResult(n, mm, A, b, c, result, lastEquation, ans, bestScore)
        print(f"isAccepted={isAccepted}, ans={ans}, bestScore={bestScore}")
        if isAccepted:
            bestResult = result
            print(f"bestResult={bestResult}")
    return [ans, bestResult]


n, mm = list(map(int, input().split()))
A = []

for i in range(n):
    A += [list(map(int, input().split()))]

b = list(map(int, input().split()))
c = list(map(int, input().split()))
 
# Bounded Solution    
#n, mm = [2,2]
#A = [[1,1], [1,-1]]
#b = [7,5]
#c = [-1,1]

# Bounded Solution
#n, mm = [2,2]
#A = [[1,1], [1,-1]]
#b = [2,2]
#c = [-1,1]

# No Solution
#n, mm = [2, 2]
#A = [[1, 1], [-1, -1]]
#b = [1, -2]
#c = [1, 1]

# Bounded Solution
#n, mm = [3,2]
#A = [[-1,-1], [1,0], [0,1]]
#b = [-1,2,2]
#c = [-1,2]

# No Solution
#n, mm = [3,3]
#A = [[-88, -2, 59], [-46, -46, 14], [37, 49, 78]]
#b = [11412, -1040, -27722]
#c = [16, 66, 95]

# Infinity
#n, mm = [1, 3]
#A = [[0, 0, 1]]
#b = [3]
#c = [1, 1, 1]


anst, ansx = solve_diet_problem(n, mm, A, b, c)

if anst == -1:
    print("No solution") # bestScore will always be -inf as none of the results satisfies all inequalities. 
    # Gaussian inequality code (function SolveEquation()) is coded such that for inequalities having no solution 
    # wrong solutions is returned which does not satify all equations
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
    

'''

############################ Sample Inputs #############################

 Bounded Solution    
n, mm = [2,2]
A = [[1,1], [1,-1]]
b = [7,5]
c = [-1,1]

 Bounded Solution
n, mm = [2,2]
A = [[1,1], [1,-1]]
b = [2,2]
c = [-1,1]

 No Solution
n, mm = [2, 2]
A = [[1, 1], [-1, -1]]
b = [1, -2]
c = [1, 1]

 Bounded Solution
n, mm = [3,2]
A = [[-1,-1], [1,0], [0,1]]
b = [-1,2,2]
c = [-1,2]

 No Solution
n, mm = [3,3]
A = [[-88, -2, 59], [-46, -46, 14], [37, 49, 78]]
b = [11412, -1040, -27722]
c = [16, 66, 95]

 Infinity
n, mm = [1, 3]
A = [[0, 0, 1]]
b = [3]
c = [1, 1, 1]

'''