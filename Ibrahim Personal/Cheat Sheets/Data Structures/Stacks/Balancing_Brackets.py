#!/bin/python3

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import deque

def isBalanced(s):

    stack = deque()
    
    for i in s:
        if i in ['(', '{', '[']: stack.append(i)  

        else:
            if not len(stack): return "NO" # for s = "}]"                   
            x = stack.pop()
            if (x=="(" and i!=")") or (x=="{" and i!="}") or (x =="[" and i!="]"): return "NO" 
                                        
    if bool(stack): return "NO" # for s = "{["
    return "YES"  

def isBalancedNoStack(s):
    # Write your code here
    for i in range(len(s)//2):
        s=s.replace('()','').replace('[]','').replace('{}','')
    if s: return 'NO' 
    else: return 'YES'

if __name__ == '__main__':
#        s = "{{[[(())]]}}"
#        s = "{[(])}"
#        s = "{{)[](}}"
#        s = "{(([])[])[]}"
        s = "{["
        print(isBalanced(s))

'''

Time Complexity - O(len(s))
Space Complexity - O(len(s))


'''    