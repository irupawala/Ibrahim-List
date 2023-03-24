# python3

EPS = 1e-6
PRECISION = 20

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
        a.append(line[:size]) # Stores each row in a list 
        b.append(line[size]) #  stores RHS of a equations in a list 
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    size = len(used_rows)
    pivot_element = Position(0, 0)
    
    for pivot_column in range(size):
        for pivot_row in range(size):
            if ((used_rows[pivot_row] == False) and (used_columns[pivot_column] == False) and a[pivot_row][pivot_column]): #We're always moving in a diagonal from left to right to select a pivot element 
                pivot_element.row = pivot_row
                pivot_element.column = pivot_column
                return pivot_element
    
    return 0
    

def SwapLines(a, b, used_rows, pivot_element):
    # This function only works when pivot element is not in the diagonal. that is when row and column of a pivot has diff values
    # This usually occurs when the variable at diagonal position is zero in a equation
    # the way we are selecting the pivot element is we are going from top to bottom for each row hence column will always have the larger value 
    # Hence bring the pivot up that is to swap the equations of a matrix we simply assign the equation in a higher position (pivot_element.column)
    # to a lower position (pivot_element.row)
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
#    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column; # After this step it is extremely important to make row = column because remember that we are 
    # moving the picot element diagonally from left top to right bottom

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    size = len(b)
    
    # Make the variable in pivot position 1 by dividing entire row by the variable in pivot position 
    
    pivot_element_divisor = a[pivot_element.row][pivot_element.column]
    for pivot_column_index in range(size):
        a[pivot_element.row][pivot_column_index] = a[pivot_element.row][pivot_column_index] / pivot_element_divisor
    b[pivot_element.row] = b[pivot_element.row] / pivot_element_divisor
    
    # Subtract other rows from the multiple of pivot row to make all other elements in pivot column equal to 0
    for row_index in range(size):
        if row_index != pivot_element.row:
            subract_divisor = a[row_index][pivot_element.column]   
            for column_index in range(size):
                a[row_index][column_index] = a[row_index][column_index] - a[pivot_element.row][column_index] * subract_divisor                
            b[row_index] =  b[row_index] - b[pivot_element.row] * subract_divisor
             
#    print(a)
#    print(b)


def MarkPivotElementUsed(pivot_element, used_rows, used_columns): # Both of them are turned true because note that we are only moving diagonally
    # for pivot element and also notice that used_rows and used_columns only represent pivot element usage
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
            return b
        
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.6f" % column[row], end = " ")

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
#    exit(0)







'''

############################ Sample Inputs #############################

2
0 1 1 
0 2 2 

4
0 0 1 0 2
1 0 0 0 0
0 0 0 1 1
0 1 0 0 6

3
2 2 4 2ww
1 4 2 4
1 1 1 4

for the equations which has no solution pivot element for any one of the element is not selected 
and hence it returns solution which does not satisfy any one of the inequality which means wrong response 
is returned

e.g.
No Solution
2
1 1 5
-1 -1 -5

3
2 2 4 2 
2 4 2 4 
4 8 4 2 

Examples to see the swapping of rows

3
0 2 4 8 
1 1 1 4 
1 1 0 2 

3
1 2 2 8
1 2 1 4
1 1 1 2 


Visit this link to solve any equations using gaussian eliminations

https://onlinemschool.com/math/assistance/equation/gaus/

########################################################################




'''