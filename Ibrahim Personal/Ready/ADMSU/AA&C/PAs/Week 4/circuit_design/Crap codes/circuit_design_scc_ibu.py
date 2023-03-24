#Uses python3

#import sys
#sys.setrecursionlimit(200000)

def post_order_to_index_convert(post_order):
    
    sorted_by_values_dict = dict(sorted(post_order.items(), key=lambda x: x[1], reverse=True))
    post_order_vertex = list(sorted_by_values_dict.keys())
    return(post_order_vertex)          
    
def explore_post_order(adj_list, visited, post_order, n, clock):
    visited[n] = True
    clock  = clock + 1 # to mark previsit 
    for x in adj_list[n]:
        if visited[x] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, x, clock)
    clock  = clock + 1        
    post_order[n] = clock
    return clock, post_order

def dfs_post_order(adj_list):

    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()}
    connected_comp = 0
    clock = 0
    #write your code here
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
            connected_comp = connected_comp + 1
        
    return post_order, connected_comp


def explore_connected_components(adj_list, visited, post_order, n, clock, scc):
    visited[n] = True
    clock  = clock + 1 # to mark previsit 
    scc.append(n)
    for x in adj_list[n]:
        if visited[x] == False:
            clock, post_order, scc = explore_connected_components(adj_list, visited, post_order, x, clock, scc)
    clock  = clock + 1        
    post_order[n] = clock
    return clock, post_order, scc

def dfs_connected_components(adj_list, post_order_vertex):
    
    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()} 
    connected_comp = 0
    clock = 0
    scc_list = []

    for x in post_order_vertex:
        scc = []
        if visited[x] == False:
            clock, post_order, scc = explore_connected_components(adj_list, visited, post_order, x, clock, scc)
            connected_comp = connected_comp + 1
            scc_list.append(scc) 
        
    return post_order, connected_comp, scc_list

def number_of_strongly_connected_components(adj, adjr):
    
    post_order_adjr, connected_comp_adjr = dfs_post_order(adjr)
    post_order_vertex = post_order_to_index_convert(post_order_adjr)
    post_order_adj, connected_comp_adj, scc_list = dfs_connected_components(adj, post_order_vertex)
#    return (connected_comp_adj)
    return(scc_list)

if __name__ == '__main__':
    
    data = list(map(int, input().split()))  
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    adj = {n:[] for n in range(1,n+1)}
    adjr = {n:[] for n in range(1,n+1)}
    for (a, b) in edges:
        adj[a].append(b)
        adjr[b].append(a) 
        
    print(number_of_strongly_connected_components(adj, adjr))
    
#################################################################################################
'''
    adj = {n:[] for n in range(1,n+1)}
    for n in range(1,n+1):
        adj[-n] = []
        
    adjr = {n:[] for n in range(1,n+1)}
    for n in range(1,n+1):
        adjr[-n] = []
    
    for (a, b) in edges:
            adj[a].append(b)
            adjr[b].append(a)
'''
####################################################################################################


     
   
    
'''
Sample Inputs

4 4 1 2 4 1 2 3 3 1 
2 4 -1 -2 2 -2 -2 1 1 2 
4 12 1 -1 1 -4 -4 3 3 1 -4 -2 -2 1 2 4 4 2 -4 4 -3 4 -3 3 2 -1 
4 4 -1 -2 -4 -1 -2 -3 -3 -1 
5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 
9 13 1 2 3 2 1 5 9 1 5 9 8 1 7 8 5 8 7 6 6 4 5 4 4 3 3 4 
'''