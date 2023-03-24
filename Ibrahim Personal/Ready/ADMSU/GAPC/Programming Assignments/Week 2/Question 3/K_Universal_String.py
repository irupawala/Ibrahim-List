#Uses python3

import sys
import threading 
sys.setrecursionlimit(200000)
import math 

def dfs(adj, current_node, path):  
    # While the current node still has outgoing edges
    while len(adj[current_node]) != 0:     
        # select the next unvisited outgoing edge
        next_node = adj[current_node].pop()
        path = dfs(adj, next_node, path)
    
    path.append(int(current_node))    
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
        return(path[::-1])
        
def createEdges(n): # Edges to be fed to heirholzer
    edges = []
    set_size = int(math.pow(2,n-1))
    for i in range(set_size):
        first_edge, second_edge = [i], [i]
        first_neighbor = (i*2)%(int(math.pow(2,n-1))) 
        second_neighbor = first_neighbor + 1
        first_edge.append(first_neighbor)
        second_edge.append(second_neighbor)
        edges.append(tuple(first_edge))
        edges.append(tuple(second_edge))       
    return edges

#if __name__ == '__main__':
def main():
    input = sys.stdin.read()
    k = int(input)
#    k = int(input())
    
    n = int(math.pow(2,k-1))
    edges = createEdges(k)
    edges = [(a+1,b+1) for (a,b) in edges]
    m = len(edges)
#    print(f"n = {n}")
#    print(f"m = {m}")
#    print(edges)
    path = heirholzer(n,m,edges)
#    print(path)
#    path_binary = [f"{i:0{k}b}" for i in path] # https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros
    path_binary = [format(i, '0' +str(k)+ 'b') for i in path] # https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros
#    print(path_binary)
    string = path_binary[0]
    for i in range(1,len(path_binary)-1):
        string = string + path_binary[i][-1] 
    print(string)
    
    
threading.Thread(target=main).start()
    
    