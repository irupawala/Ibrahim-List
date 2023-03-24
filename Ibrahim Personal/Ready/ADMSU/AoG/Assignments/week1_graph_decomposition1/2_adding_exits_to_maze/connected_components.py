#Uses python3

import sys

'''
Runtime is O(|V| + |E|)
'''

def explore(i, adj, visited):
    visited[i] = True
    for y in adj[i]:
        if not visited[y]:
            explore(y, adj, visited)


def number_of_components(adj):
#    result = 0
    #write your code here
    visited = [False] * len(adj)
    cc = 0
    for i in range(len(adj)):
        if not visited[i]:
            explore(i, adj, visited)
            cc += 1
            
    return cc

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
