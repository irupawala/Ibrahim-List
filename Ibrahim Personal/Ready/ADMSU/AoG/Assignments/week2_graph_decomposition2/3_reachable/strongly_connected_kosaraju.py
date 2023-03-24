'''

- To Understand Visit - https://www.geeksforgeeks.org/strongly-connected-components/
- Notice that Kosaraju's Algo is same as the one discussed in the lecture's slide only difference is 
post-order numbering is performed on G while SCC's are computed on GR.
- Time Complexity - O(|V|+|E|)

'''



def post_order_to_index_convert(post_order):   
    sorted_by_values_dict = dict(sorted(post_order.items(), key=lambda x: x[1], reverse=True))
    post_order_vertex = list(sorted_by_values_dict.keys())
    print(f"post_order_vertex = {post_order_vertex}")
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
    print(f"adj_list = {adj_list}")
    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()}
    clock = 0
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
    
    print(f"post_order = {post_order}")
    return post_order

def explore_connected_components(adj_list, visited, n, scc):
    visited[n] = True
    scc.append(n)
    for x in adj_list[n]:
        if visited[x] == False:
            scc = explore_connected_components(adj_list, visited, x, scc)
    return scc

def dfs_connected_components(adj_list, post_order_vertex):   
    visited = {n:False for n in adj_list.keys()}
    scc_list = []

    for x in post_order_vertex:
        scc = []
        if visited[x] == False:
            scc = explore_connected_components(adj_list, visited, x, scc)
            scc_list.append(scc) 
        
    return scc_list

def kosaraju_algo(adj, adjr): 
    post_order_adj = dfs_post_order(adj)
    post_order_vertex = post_order_to_index_convert(post_order_adj)
    
    scc_list = dfs_connected_components(adjr, post_order_vertex)
    print(f"scc_list = {scc_list}")
    return(len(scc_list))
    
    
if __name__ == '__main__':
    data = [9, 10, 1, 2, 2, 3, 3, 4, 4, 1, 3, 5, 5, 6, 6, 7, 7, 5, 8, 7, 8, 9]
#    data = [10, 15, 1, 2, 2, 3, 3, 10, 10, 1, 3, 1, 3, 4, 4, 5, 5, 6, 6, 4, 6, 3, 5, 7, 7, 8, 8, 9, 9, 5, 8, 5]
    
#    data = [8, 13, 1, 2, 2, 1, 1, 3, 3, 4, 2, 4, 5, 3, 4, 5, 5, 6, 4, 6, 5, 7, 7, 6, 6, 8, 8, 7]
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(f"edges = {edges}")
    adj = {n:[] for n in range(n)}
    adjr = {n:[] for n in range(n)}
    for (a, b) in edges:        
        adj[a - 1].append(b - 1)
        adjr[b - 1].append(a - 1)

    print(kosaraju_algo(adj, adjr))
    

