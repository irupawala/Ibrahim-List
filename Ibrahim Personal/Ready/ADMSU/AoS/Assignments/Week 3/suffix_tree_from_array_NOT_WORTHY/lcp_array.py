# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:19:20 2021

@author: 1000249643
"""

def SortCharacters(S):
    
    S = list(S)
    Order = [-1] * len(S)
    char_set = sorted(list(set(S)))
    count = [S.count(x) for x in char_set]
             
    for j in range(1, len(count)):
        count[j] += count[j-1]
           
    for i in reversed(range((len(S)))):
        c = S[i]
        cl = char_set.index(c)
        count[cl] -= 1
        Order[count[cl]] = i 
          
    return Order

def ComputeCharClasses(S, Order):
    
    n = len(S)
    Class = [0] * n
    Class[Order[0]] = 0
    
    for i in range(1, n):
        cur = Order[i]
        prev = Order[i-1]
        
        if S[cur] != S[prev]:
            Class[cur] = Class[prev] + 1
        else:
            Class[cur] = Class[prev] 
            
    return Class
    
def SortDoubled(S, L, Order, Class):
    
    count = [0] * len(S)
    newOrder = [-1] * len(S)
#    char_set = set(Class) 
#    count = [Class.count(x) for x in char_set] # using any of the two methods, index of class refers to class # while the value itself refers to the number of repeats (count)
    for i in range(len(S)):
        count[Class[i]] += 1              
    
    for j in range(1, len(count)):
        count[j] = count[j] + count[j-1]   
        
    for i in reversed(range(len(S))): # we need to go in reverse order because it is important for sort to be stable
        start = (Order[i] - L + len(S)) % len(S) #iterating from the last element in the reverse order of the second half
        cl = Class[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
        
    return newOrder
        
def UpdateClasses(newOrder, Class, L):
    
    n = len(newOrder)
    newClass = [0] * n
    newClass[newOrder[0]] = 0
    
    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = cur + L
        midPrev = (prev + L) % n
        
        if (Class[cur] != Class[prev] or Class[mid] != Class[midPrev]):
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
            
    return newClass

def build_suffix_array(S):
    
    Order = SortCharacters(S)
    Class = ComputeCharClasses(S, Order)
    
    L = 1
    
    while L < len(S):
        Order = SortDoubled(S, L, Order, Class)
        Class = UpdateClasses(Order, Class, L)
        L = 2*L
        
    return Order



def InvertSuffixArray(order):
    pos = [-1] * len(order) 
    for i in range(len(pos)):
        pos[order[i]] = i
    return pos
    
def LCPOfSuffixes(S, i, j, equal):
    lcp = max(0, equal)
    i_upper = i+lcp 
    j_upper = j+lcp
    while ((i_upper < len(S)) and (j_upper < len(S))):
        if S[i_upper] == S[j_upper]:
            lcp = lcp + 1
            i_upper = i+lcp 
            j_upper = j+lcp
        else:
            break
    return lcp
    

def ComputeLCPArray(S, order):
    lcpArray = [-1] * (len(S) - 1)
    lcp = 0
    posInOrder = InvertSuffixArray(order) # pos stores the index of order in the ascending order 
    suffix = order[0]
    
    for i in range(len(S)):
        orderIndex = posInOrder[suffix]
        if orderIndex == len(S)-1:
            lcp = 0 # if last element in suffix array is reached, reset LCP, increase suffix count by 1 and continue
            suffix = (suffix + 1) % len(S)
            continue
        nextSuffix = order[orderIndex + 1]
        lcp = LCPOfSuffixes(S, suffix, nextSuffix, lcp-1)
        lcpArray[orderIndex] = lcp
        suffix = (suffix + 1) % len(S)
        
    return lcpArray
    
    return 0
    


if __name__ == "__main__":
    S = input().strip()
#    S = "ababdabc"
    order = build_suffix_array(S)
    print(order)
#    order = [0, 5, 2, 1, 6, 3, 7, 4]
#    order = [6, 5, 4, 2, 0, 3, 1]
    lcpArray = ComputeLCPArray(S, order)
    print(lcpArray)
    