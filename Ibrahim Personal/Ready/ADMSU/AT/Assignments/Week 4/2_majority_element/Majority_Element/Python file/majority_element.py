# Uses python3
import sys, math


def merge_majority_finder (a, b):
    counter = 0
    majority_element = 0
    majority_element_a = a[len(a)-1]
    majority_element_b = b[len(b)-1]
    a.pop()
    b.pop()
    
    
    
    if ((majority_element_a == majority_element_b) & (majority_element_a != -1)):
        a = a + b
        a.append(majority_element_a)
        return a
    
    elif ((majority_element_a == -1) & (majority_element_b == -1) & (len(a) != 1) & (len(b) != 1) ):
        a = a + b
        a.append(majority_element_a)
        return a
        
    else:
       # a.append(b)
        a = a + b
        for i in a:
            for j in a:
                if (i == j):
                    counter+=1
                
                if (counter > int(len(a)/2)):
                    majority_element = i
                    a.append(majority_element)
                    return a
             
            counter = 0
        a.append(-1)
        return a
                    
                


def majority_element_finder (a):
    a.pop()
    
    if (len(a) == 1):
        a.append(-1)
        return a
    
    mid = int(len(a)/2)
    b = a[ : mid]
    c = a[mid : ]
    b.append(-1)
    c.append(-1)
    

    b = majority_element_finder(b);
    c = majority_element_finder(c);
    a = merge_majority_finder(b, c)
    return a

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    a.append(-1) 
    a = majority_element_finder(a)
    
    return (a[len(a) - 1])


if __name__ == '__main__':
    
    '''
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    '''
   
    # number of elements 
    # n = int(input("Enter number of elements : ")) 

    # Below line read inputs from user using map() function 
    n, *a = list(map(int, input("\nEnter the numbers : ").split()))
    


    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)