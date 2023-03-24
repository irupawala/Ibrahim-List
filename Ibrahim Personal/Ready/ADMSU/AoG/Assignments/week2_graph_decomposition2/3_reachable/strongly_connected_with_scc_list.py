'''
- Same as the one discussed in lecture whilst also printing the scc list (and not just count)
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
    connected_comp, clock = 0, 0
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
            connected_comp = connected_comp + 1
    
    print(f"post_order = {post_order}, connected_comp = {connected_comp}")
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
    connected_comp, clock, scc_list = 0, 0, []

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
    print(f"scc_list = {scc_list}")
    return(connected_comp_adj)
    
    
if __name__ == '__main__':
#def main():
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))  
#    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    data = [9, 13, 1, 2, 3, 2, 1, 5, 9, 1, 5, 9, 8, 1, 7, 8, 5, 8, 7, 6, 6, 4, 5, 4, 4, 3, 3, 4]
#    data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
#    data = [9, 10, 1, 2, 2, 3, 3, 4, 4, 1, 3, 5, 5, 6, 6, 7, 7, 5, 8, 7, 8, 9]
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = {n:[] for n in range(n)}
    adjr = {n:[] for n in range(n)}
    for (a, b) in edges:
#        adj.setdefault(a - 1, [])
#        adjr.setdefault(b - 1, [])
        
        adj[a - 1].append(b - 1)
        adjr[b - 1].append(a - 1)
    
#    print(adj)
#    print(adjr)    
    print(number_of_strongly_connected_components(adj, adjr))
    
#    print(number_of_strongly_connected_components(adj))

#threading.Thread(target=main).start()     
    
'''

Sample Inputs

4 4 1 2 4 1 2 3 3 1 
5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 
9 13 1 2 3 2 1 5 9 1 5 9 8 1 7 8 5 8 7 6 6 4 5 4 4 3 3 4 

'''