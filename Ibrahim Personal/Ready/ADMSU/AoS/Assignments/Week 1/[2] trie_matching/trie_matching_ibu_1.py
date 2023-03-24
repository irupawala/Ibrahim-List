# python3

import sys

NA = -1

class Node():
    def __init__ (self):
        self.next = [NA] * 4
        
def build_trie(patterns):
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
    len_counter = 0
    
    while True:
        if trie[v] == {}:
            return len_counter,True
        elif symbol in trie[v]:
            v = trie[v][symbol]
            symbol_index += 1
            symbol = text[symbol_index]
            len_counter += 1
        else:
            return 0, False
    

def solve (text, n, patterns):
    
    result = []    
    trie = build_trie(patterns)
    pattern_match_decision = False
#    print(trie)

    for index, x in enumerate(text):
        shortened_text = text[index:]
        pattern_match_decision, len_counter = prefix_trie_matching(shortened_text, trie)
        if pattern_match_decision:
            result.append(index)
            index_addition = len_counter - 1
            index = index + index_addition

    return result


if __name__ == "__main__":

    text = sys.stdin.readline ().strip ()
    n = int (sys.stdin.readline ().strip ())   
    patterns = [] 
    
    for i in range (n):        
        patterns += [sys.stdin.readline ().strip ()]
       
    
    ans = solve (text, n, patterns)
    sys.stdout.write (' '.join (map (str, ans)) + '\n')
    
 
#    text = input().strip()
#    n = int(input().strip())    
#    patterns = [] 
#
#    for i in range(n):
#        patterns.append(str(input()))
#            
##    print(patterns)   
#    ans = solve (text, n, patterns)
#    print(ans)