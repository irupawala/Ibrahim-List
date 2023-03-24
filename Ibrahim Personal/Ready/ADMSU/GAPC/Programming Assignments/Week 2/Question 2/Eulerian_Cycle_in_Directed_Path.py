#Uses python3

import sys
import threading
sys.setrecursionlimit(200000)

def dfs(adj, current_node, path):  
    # While the current node still has outgoing edges
    while len(adj[current_node]) != 0:     
        # select the next unvisited outgoing edge
        next_node = adj[current_node].pop()
        path = dfs(adj, next_node, path)
    
    path.append(int(current_node) + 1)    
    return path

def graphHasEulerianCycle(in_degree, out_degree):
    for i in range(len(in_degree)):
        diff = in_degree[i] - out_degree[i]
        if diff != 0 : return 0 # For Eulerian Cycle in_degree = out_degree
    return 1

def createAdjacencyList(n,m,edges):
    adj = [[] for _ in range(n)] # Creating Adjacency list
    in_degree = [0 for _ in range(n)]
    out_degree = [0 for _ in range(n)]
    
    for (a, b) in edges:
        adj[a-1].append(b-1)
        out_degree[a-1] += 1
        in_degree[b-1] +=1     
        
    return adj, in_degree, out_degree

def heirholzer(n,m,edges):
    
    adj, in_degree, out_degree = createAdjacencyList(n,m,edges)
    eulerian_exists = graphHasEulerianCycle(in_degree, out_degree)
    
    if eulerian_exists: 
        path = dfs(adj, 0, [])[1:]
        print(1)
        print(" ".join(map(str,path[::-1])))
    else: print(0)    

#if __name__ == '__main__':
def main():    
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*m):2], data[1:(2*m):2]))
    
    heirholzer(n,m,edges)

threading.Thread(target=main).start()  
    
    
'''
Sample Inputs

4 7 2 3 3 4 1 4 3 1 4 2 2 3 4 2
4 7 1 2 2 1 1 4 4 1 2 4 3 2 4 3 
6 12 1 2 2 2 2 4 2 4 1 3 3 1 3 2 4 3 4 6 6 3 3 5 5 6 

'''

# Note that this algo is more efficient (linear time) even compared to one discussed in lectures (Ants Problem)