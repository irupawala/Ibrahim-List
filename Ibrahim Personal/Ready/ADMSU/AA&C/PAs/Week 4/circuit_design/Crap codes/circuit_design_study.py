# python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(1100000) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

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
#    print(f"adj_list = {adj_list}")
    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()}
    connected_comp, clock = 0, 0
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
            connected_comp = connected_comp + 1
    
#    print(f"post_order = {post_order}, connected_comp = {connected_comp}")
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
#    print(f"scc_list = {scc_list}")
    return(scc_list)
    
def implicationGraph(n, clauses):

    adj, adjr  = {}, {}
    for n in range(1,n+1):
#        adj[n], adj[-n] = [], []
#        adjr[n], adjr[-n] = [], []
        
        adj[-n], adj[n] = [], []
        adjr[-n], adjr[n] = [], []        


    for x in clauses:
        if len(x) == 2: # For each 2-Clause
            l1 = x[0]
            l2 = x[1]            
            # -l1 --> l2
            adj[-l1].append(l2)
            adjr[l2].append(-l1)              
            # -l2 --> l1
            adj[-l2].append(l1)
            adjr[l1].append(-l2)    
        
        if len(x) == 1:
           l1 = x[0]
           adj[-l1].append(l1) 
           adjr[l1].append(-l1)
    
#    print(f"adj = {adj}")
#    print(f"adjr = {adjr}")
    return adj, adjr
    
def SAT_2_CNF(n, clauses):
    
    adj, adjr = implicationGraph(n, clauses)
    scc_list = number_of_strongly_connected_components(adj, adjr)    
#    print(f"scc_list = {scc_list}")    
    for x in range(1,n+1):
        for scc in scc_list:
            if ((x in scc) and (-x in scc)):
                return None
                
    literals = {n:None for n in  range(1, n+1)}
    for scc in scc_list:
        for literal in scc:            
            index = abs(literal)
            if literals[index] == None:
                literals[literal] = 0
                literals[-literal] = 1

    return(list(literals.values()))

if __name__ == "__main__":
#def main():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
#    n, m = 3, 4    
#    clauses = [[2, 1], [-2], [-1, -2], [-1]]
    result = SAT_2_CNF(n, clauses)
#    print(f"result = {result}")

    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        result_list = [-i-1 if result[i] else i+1 for i in range(n)]
        print(" ".join(map(str, result_list)))
        
#threading.Thread(target=main).start()