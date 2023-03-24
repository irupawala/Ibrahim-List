# python3
import sys

"""
Time Complexity - O(|S|log|S|)

- Initialization: SortCharacters in O(|S|+|Σ|) and ComputeCharClasses in O(|S|)
- While loop iteration: SortDoubled and UpdateClasses run in O(|S|)
- O(log|S|) iterations while L < |S|
- Hence total time is O(|S|+|Σ|) + O(|S|) + O(log|S|)(|S| + |S|) =~ O(|S|log|S|)

Space Complexity - O(|S|) as compared to O(|S^2|) using the normal method.

"""



def SortCharacters(S): # Running Time - O(|S| + |char_set|)
    
    S = list(S)
    Order = [-1] * len(S)
    char_set = sorted(list(set(S)))
    count = [S.count(x) for x in char_set]
             
    for j in range(1, len(count)):
        count[j] += count[j-1]
           
    for i in reversed(range((len(S)))): # Necessary to do this reverse because similar char with lower index should 
                                        # come first in suffix array
        c = S[i]
        cl = char_set.index(c)
        count[cl] -= 1
        Order[count[cl]] = i 
          
    return Order

def ComputeCharClasses(S, Order): # Running Time - O(|S|)
    
    n = len(S)
    Class = [-1] * n
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
    char_set = set(Class) 
    count = [Class.count(x) for x in char_set] # using any of the two methods, index of class refers to class # while the value itself refers to the number of repeats (count)
#    for i in range(len(S)):
#        count[Class[i]] += 1              
    
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
    newClass = [-1] * n
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


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
#  text = input().strip() 
  print(" ".join(map(str, build_suffix_array(text))))
  
  
"""
ababaa$
AAA$
GAC$
GAGAGAGA$
AACGATAGCGGTAGA$

"""

