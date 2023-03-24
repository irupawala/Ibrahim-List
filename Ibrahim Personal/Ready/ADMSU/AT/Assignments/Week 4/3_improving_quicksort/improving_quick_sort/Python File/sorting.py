# Uses python3
#import sys
import random
#from itertools import chain

            
def partition3(a, l, r):
    m = []
    x = a[l] # kth element which was swapped with first element
    j = l
    k = l    
    
#    print (f"x = {x}, l = {l}, r = {r}")
#    print("Input Array")
#    for i in a:
#        print(i, end=' ')
#    print ("\n")   
    
    for i in range(l + 1, r + 1): # r + 1 because last element is not considered in range 
#        print(f"i = {i}")
#        print(f"a[i] = {a[i]}")
#        print(f"x = {x}")
        if a[i] == x:
#            print("Here equal")
            j += 1
            a[i], a[j] = a[j], a[i]
            
        if a[i] < x:
#            print("Here less")
            a.insert(l, a[i])
            a.pop(i+1)

            j += 1
            k += 1            

#        print(f"Array in loop {i}")
#        for i in a:
#            print(i, end=' ')              
#        print ("\n")     


#    print ("\n")      
#    print("===================================Returned Array=============================")
#    for i in a:
#        print(i, end=' ')              
#    print ("\n")     
    
    m.append(k)
    m.append(j)
    return m


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x: # Region where a[i] <= x 
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
    
    
def randomized_quick3_sort(a, l, r):
    if l >= r:
        return
    m = []
    k = random.randint(l,r)
    a[l], a[k] = a[k], a[l] # Swap the first element with the element at kth position
    m = partition3(a, l, r)

    m1 = m[0]
    m2 = m[1]
#    print(f"\nm1 = {m1}")
#    print(f"m2 = {m2}")
#    print(f"k = {k}")
    
    randomized_quick3_sort(a, l, m1 - 1);
    randomized_quick3_sort(a, m2 + 1, r);
        
    
    


if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *a = list(map(int, input("Enter first number of elements and then all the elements: ").split()))
   # n, *a = list(map(int, input.split()))
    
    #randomized_quick_sort(a, 0, n - 1)
    randomized_quick3_sort(a, 0, n - 1)
#    print ("\n")      
#    print("Final Array")    
    for x in a:
        print(x, end=' ')
        
        

##################################################### Random Tests: #####################################################

       
#    while(1):      
#    
#        n = random.randrange(0, 100, 1)
#        print (f"n = {n}")
#
#        
#        a1 = []
#        a2 = []
#        for i in range(n):
#            k = random.randint(1, 1000)
#            a1.append(k)
#            a2.append(k)
#        
#        print('a1 = ')
#        for x in a1:
#            print(x, end=' ')
#        print('\n')
#        
#        print('a2 = ')
#        for x in a2:
#            print(x, end=' ')
#        print('\n')        
#        
#
#        randomized_quick_sort(a1, 0, n - 1)
#        randomized_quick3_sort(a2, 0, n - 1)
#        
#        
#        print('a1 = ')        
#        for i in a1:
#            print(i, end=' ')
#        print('\n')
#        
#        print('a2 = ')                
#        for i in a2:
#            print(i, end=' ')            
#        print('\n')
#        
#        if (a1 == a2):
#            print("====OK====")
#        else:
#            print("===========================================Wrong Answer========================================")
#            break
#        
        

        