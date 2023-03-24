# python3

#import sys

'''
Patterns Trie Matching

Running Time - O(|Text|*|Longest Pattern|)
Running Time of Trie Construction - O(|Sum of patterns length|)
Memory Footprint - O(|Sum of patterns length|)

'''


class Node:
    def __init__(self, id, child, pattern_end):
        self.id = id
        self.child = child
        self.pattern_end = pattern_end

def build_trie(patterns): # Building Trie of patterns
    trie = dict()
    # write your code here
    
    trie[0] = Node(0, {}, False)
    counter = 0
    
    for pattern in patterns:
        currentNode = 0
        for index, letter in enumerate(pattern):
            currentSymbol = letter
            if currentSymbol in trie[currentNode].child:
                currentNode = trie[currentNode].child[currentSymbol]
            else:
                counter += 1
                trie[currentNode].child[currentSymbol] = counter
                trie[counter] = Node(counter, {}, False)
                currentNode = counter   
                
            if index == len(pattern)-1:
                trie[currentNode].pattern_end = True
                
    return trie

def prefix_trie_matching(text, trie):
    
    text += "$"
    symbol_index = 0
    symbol = text[symbol_index]
    v = 0 # root of the tree
    
    while True:
        if trie[v].pattern_end : # Checking if the last node is a leaf (no further childs)
            return True
        elif symbol in trie[v].child:
            v = trie[v].child[symbol]
            symbol_index += 1
            symbol = text[symbol_index]
        else:
            return False
    

def solve (text, n, patterns):  
    
    result = []    
    trie = build_trie(patterns)

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