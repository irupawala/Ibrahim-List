# python3
#import sys

'''
This Problem is demonstrates very smart use of Dictionaries.
Also Notice that you can keep tuples itself as a key for dictionaries

Running Time - O(|Text|)
Memory - 2|Text|

'''

def InverseBWT(bwt):
    # write your code here

    index_list = list(range(len(bwt)))
    last = list(zip(bwt, index_list))
    first = sorted(last)
    first_to_last = {f: l for f, l in zip(first, last)} # Notice that this was the step which lead to passing the time limit 
    
    result = ['$'] * len(last) # Note that creating a list of elements and then making string out of it is the fastest  
#    result = ''
    next = first[0]
    
    
    for x in range(len(bwt)):
            
            result[x] = next[0]
#            result = ''.join((result[x][0], result))
#            result += next[0] # avoid appending to strings as far as possible
#            next = first.index(next) # Finding index from list is extremely slow. Create dictionary instead is wise
            next = first_to_last[next]
    
    result = ''.join(result)  
    return (result[::-1])


if __name__ == '__main__':
#    bwt = sys.stdin.readline().strip()
    bwt = input().strip()
    
    print(InverseBWT(bwt))
    
