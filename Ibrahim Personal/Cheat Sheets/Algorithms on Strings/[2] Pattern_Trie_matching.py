# python3

#import sys

'''
Patterns Trie Matching

Running Time - O(|Text|*|Longest Pattern|)
Running Time of Trie Construction - O(|Sum of patterns length|)
Memory Footprint - O(|Sum of patterns length|)

'''

def build_trie(patterns): # Building Trie of patterns
    trie = dict()
    # write your code here
    
    trie[0] = {}
    counter = 0
    
    for pattern in patterns:
        currentNode = 0
        for index, letter in enumerate(pattern):
            currentSymbol = letter
            if currentSymbol in trie[currentNode]:
                currentNode = trie[currentNode][currentSymbol]
            else:
                counter += 1
                trie[currentNode][currentSymbol] = counter
                trie[counter] = {}
                currentNode = counter   
    return trie

def prefix_trie_matching(text, trie):
    
    text += "$"
    symbol_index = 0
    symbol = text[symbol_index]
    v = 0 # root of the tree
    
    while True:
        if trie[v] == {}: # Checking if the last node is a leaf (no further childs)
            return True
        elif symbol in trie[v]:
            v = trie[v][symbol]
            symbol_index += 1
            symbol = text[symbol_index]
        else:
            return False
    

def solve (text, n, patterns):  
    
    result = []    
    trie = build_trie(patterns)
#    print(trie)

    for index, x in enumerate(text): # Checking each substring of text from index to end of the string in pattern Trie
        shortened_text = text[index:]
        if prefix_trie_matching(shortened_text, trie):
            result.append(index)

    return result


if __name__ == "__main__":

#    text = sys.stdin.readline ().strip ()
#    n = int (sys.stdin.readline ().strip ())   
#    patterns = [] 
#    
#    for i in range (n):        
#        patterns += [sys.stdin.readline ().strip ()]
#       
#    
#    ans = solve (text, n, patterns)
#    sys.stdout.write (' '.join (map (str, ans)) + '\n')
    
 
    text = input().strip()
    n = int(input().strip())    
    patterns = [] 

    for i in range(n):
        patterns.append(str(input()))
            
#    print(patterns)   
    ans = solve (text, n, patterns)
    print(ans)