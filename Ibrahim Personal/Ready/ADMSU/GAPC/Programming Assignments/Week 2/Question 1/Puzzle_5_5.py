# python3

# Program Implementation is correct However, it is not accepted by the Grader becasue of output format not proper error
# When given the input used by grader the code generates correct output
# Replicated exactly the way input is taken and output is printed by the passing solution still not accepted

import sys 
from math import sqrt

def _input():
    data = sys.stdin.read().strip().split('\n') # This means though input is given in separate line they're separated by new line Char '\n'
    n = int(sqrt(len(data))) # n here is thus len of input which is 25
    blocks = []
    for d in data:
        blocks.append(d[1:-1].split(','))
    return n, blocks

def output_print(output):
    x = sorted(output)
    for index in range(1,len(x)+1):
        if index % 5 == 0:
            k = output[index-1]
            k = str(k)
            k = k.replace("[", "(").replace("]", ")").replace(" ", "")
            print(k)
        else:
            k = output[index-1]
            k = str(k)
            k = k.replace("[", "(").replace("]", ")").replace(" ", "")
            print(k, end=";")
        
def printResultNew(ans):
    for index in range(1,len(ans)+1):
        if index % 5 == 0:
            print('('+','.join(ans[index-1])+')')
        else:
            print('('+','.join(ans[index-1])+')', end=";")

def puzzle_solver(input_list):
    
    output_dict = {}
    
    # Filtering out the border squares with two black surfaces
    for l1 in input_list:
        if l1[0] == 'black' and l1[1] == 'black':
            output_dict[0] = l1
        elif l1[1] == 'black' and l1[2] == 'black':
            output_dict[20] = l1
        elif l1[2] == 'black' and l1[3] == 'black':
            output_dict[24] = l1
        elif l1[0] == 'black' and l1[3] == 'black':
            output_dict[4] = l1
            
    # Filtering out inner border squares with one black surfaces and adjacent to l1
    for l2 in input_list:
        if l2[0] == 'black':
            if l2[1] == output_dict[0][3]:
                output_dict[1] = l2
            if l2[3] == output_dict[4][1]:
                output_dict[3] = l2
        elif l2[2] == 'black':
            if l2[1] == output_dict[20][3]:
                output_dict[21] = l2
            if l2[3] == output_dict[24][1]:
                output_dict[23] = l2
                
        elif l2[1] == 'black':
            if l2[0] == output_dict[0][2]:
                output_dict[5] = l2
            if l2[2] == output_dict[20][0]:
                output_dict[15] = l2
        elif l2[3] == 'black':
            if l2[0] == output_dict[4][2]:
                output_dict[9] = l2 
            if l2[2] == output_dict[24][0]:
                output_dict[19] = l2
    
    # squares between two l2 and at the border of the "Valid Arrangement"
    for l3 in input_list:
        if l3[0] == 'black' and l3[1] == output_dict[1][3] and l3[3] == output_dict[3][1]:
            output_dict[2] = l3
        if l3[1] == 'black' and l3[0] == output_dict[5][2] and l3[2] == output_dict[15][0]:
            output_dict[10] = l3
        if l3[2] == 'black' and l3[1] == output_dict[21][3] and l3[3] == output_dict[23][1]:         
            output_dict[22] = l3
        if l3[3] == 'black' and l3[0] == output_dict[9][2] and l3[2] == output_dict[19][0]:
            output_dict[14] = l3
            
   # squares touching sides of two l2's   
        if l3[0] == output_dict[1][2] and l3[1] == output_dict[5][3]:
            output_dict[6] = l3
        if l3[0] == output_dict[3][2] and l3[3] == output_dict[9][1]:
            output_dict[8] = l3            
        if l3[1] == output_dict[15][3] and l3[2] == output_dict[21][0]:
            output_dict[16] = l3
        if l3[3] == output_dict[19][1] and l3[2] == output_dict[23][0]:
            output_dict[18] = l3
            
    # squares between 3 l3's        
    for l4 in input_list:
        if l4[0] == output_dict[2][2] and l4[1] == output_dict[6][3] and l4[3] == output_dict[8][1] :
            output_dict[7] = l4
        if l4[0] == output_dict[6][2] and l4[1] == output_dict[10][3] and l4[2] == output_dict[16][0]:
             output_dict[11] = l4
        if l4[1] == output_dict[16][3] and l4[2] == output_dict[22][0] and l4[3] == output_dict[18][1]:
            output_dict[17] = l4
        if l4[0] == output_dict[8][2] and l4[2] == output_dict[18][0] and l4[3] == output_dict[14][1]:
            output_dict[13] = l4
            
    # square between 4 l4's               
    for l5 in input_list:
        if l5[0] == output_dict[7][2] and l5[1] == output_dict[11][3] and l5[2] == output_dict[17][0] and l5[3] == output_dict[13][1]:
            output_dict[12] = l5
    
    return output_dict

if __name__ == "__main__":
    
    
    # Sample Input
    input_list_1 = [['black','black','blue','cyan'], 
                    ['black','brown','maroon','red'], 
                    ['black','cyan','yellow','brown'], 
                    ['black','red','green','black'], 
                    ['black','red','white','red'], 
                    ['blue','black','orange','yellow'], 
                    ['blue','cyan','white','black'], 
                    ['brown','maroon','orange','yellow'], 
                    ['green','blue','blue','black'], 
                    ['maroon','black','yellow','purple'], 
                    ['maroon','blue','black','orange'], 
                    ['maroon','orange','brown','orange'], 
                    ['maroon','yellow','white','cyan'], 
                    ['orange','black','maroon','cyan'], 
                    ['orange','orange','black','black'], 
                    ['orange','purple','maroon','cyan'], 
                    ['orange','purple','purple','purple'], 
                    ['purple','brown','black','blue'], 
                    ['red','orange','black','orange'], 
                    ['white','cyan','red','orange'], 
                    ['white','orange','maroon','blue'], 
                    ['white','orange','orange','black'], 
                    ['yellow','black','black','brown'], 
                    ['yellow','cyan','orange','maroon'], 
                    ['yellow','yellow','yellow','orange']]
    

    n, blocks = _input()
    output = puzzle_solver(blocks)
#    print(output)
    printResultNew(output)