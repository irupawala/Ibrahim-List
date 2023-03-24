#Uses python3

#import sys

'''
Runtime is O(|V| + |E|)
'''


def dfs(adj, used, order, x):
    #write your code here
    used[x] = True
    for neighbor in adj[x]:
        if used[neighbor] == False:
            dfs(adj, used, order, neighbor)
    order.append(x)
    return order


def toposort(adj):
    used = [False] * len(adj)
    order = []
    #write your code here
    for index, vertex in enumerate(adj):
        if used[index] == False:
            dfs(adj, used, order, index)
    return order

if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    data = list(map(int, input().split()))  
    
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
#    order = toposort(adj).reverse()
    order = toposort(adj)
    for x in reversed(order):
        print(x + 1, end=' ')
        
###################################################################
## Sample Inputs ##
'''
5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3
4 3 1 2 4 1 3 1
4 1 3 1 
7 6 1 2 2 5 3 4 4 5 5 6 6 7 
'''

