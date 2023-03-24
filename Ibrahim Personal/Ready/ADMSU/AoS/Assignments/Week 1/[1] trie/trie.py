#Uses python3
#import sys

'''
Trie of Patterns 
Running time - O(sum of patterns)
'''


def build_trie(patterns):
    tree = dict()
    # write your code here
    
    tree[0] = {}
    counter = 0
    
    for pattern in patterns:
        currentNode = 0
        for index, letter in enumerate(pattern):
            currentSymbol = letter
            if currentSymbol in tree[currentNode]:
                currentNode = tree[currentNode][currentSymbol]
            else:
                counter += 1
                tree[currentNode][currentSymbol] = counter
                tree[counter] = {}
                currentNode = counter
    
    return tree


if __name__ == '__main__':
    
#    patterns = sys.stdin.read().split()[1:]
    
    patterns = input().split()[1:] 
    
    # 3 'AT' 'AG' 'AC'
    # 3 'ATAGA' 'ATC' 'GAT'

    tree = build_trie(patterns)
#    print(tree)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
