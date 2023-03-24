#Uses python3

'''
Runtime is O(|V| + |E|)
'''

import sys

def DFS(adj_list, x, y):
    
    def explore(adj_list, v, y):
        visited[v] = True
        for w in adj_list[v]: # First checking if the neighbor itself has final destination node
            if visited[w] != True:
                if w == y:
                    return True 
                else:
                    if (explore(adj_list, w, y)): return True
        
        return False
    
    visited = [False] * len(adj_list)    
    for index, vertex in enumerate(adj_list):
        if index == x:
            if visited[index] != True: # If not visited    
                if (explore(adj_list, index, y) == True):
                    return True
    return False
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#    data = list(map(int, input().split()))
    n, m = data[0:2]
    x, y = data[-2:]
    data = data[2:len(data)-2]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)] # Creating Adjacency list
    x, y = x - 1, y - 1 # Making all the numbers base 0 (meaning 1 will be treated as 0) to facilitate ease of iterating over a loop
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
        
    if(DFS(adj, x, y)):
        print (1)
    else:
        print (0)
    
#    print("Press Any Key to Exit")