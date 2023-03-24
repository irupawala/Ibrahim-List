#Uses python3

#import sys
#import threading
#sys.setrecursionlimit(200000)

'''
- Same as the one discussed in lecture
- Time Complexity - O(|V|+|E|)
'''

def post_order_to_index_convert(post_order):
    post_order_index = [_ for _ in range(len(post_order))]
    zipped_list = list(zip(post_order_index, post_order))
    zipped_list.sort(key = lambda x: x[1], reverse = True)
    post_order_index = [x[0] for x in zipped_list]
    return(post_order_index)          
    
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
    
    visited = [False] * len(adj_list)
    post_order = [-1] * len(adj_list)
    connected_comp = 0
    clock = 0
    #write your code here
    for index, vertex in enumerate(adj_list):
        if visited[index] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, index, clock)
            connected_comp = connected_comp + 1
        
    return post_order, connected_comp


def explore_connected_components(adj_list, visited, post_order, n, clock):
    visited[n] = True
    clock  = clock + 1 # to mark previsit 
    for x in adj_list[n]:
        if visited[x] == False:
            clock, post_order = explore_connected_components(adj_list, visited, post_order, x, clock)
    clock  = clock + 1        
    post_order[n] = clock
    return clock, post_order

def dfs_connected_components(adj_list, post_order_index):
    
    visited = [False] * len(adj_list)
    post_order = [-1] * len(adj_list)
    connected_comp = 0
    clock = 0
    #write your code here
    for x in post_order_index:
        if visited[x] == False:
            clock, post_order = explore_connected_components(adj_list, visited, post_order, x, clock)
            connected_comp = connected_comp + 1
        
    return post_order, connected_comp

def number_of_strongly_connected_components(adj, adjr):
#    result = 0   #write your code here
    
    post_order_adjr, connected_comp_adjr = dfs_post_order(adjr)
    post_order_index = post_order_to_index_convert(post_order_adjr)
#    print (post_order_index)
#    post_order_index = [1, 8, 7, 6, 0, 3, 2, 5, 4]
    post_order_adj, connected_comp_adj = dfs_connected_components(adj, post_order_index)

    
    return (connected_comp_adj)

if __name__ == '__main__':
#def main():
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    data = list(map(int, input().split()))  
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjr = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adjr[b - 1].append(a - 1)
        
    print(number_of_strongly_connected_components(adj, adjr))
    
#    print(number_of_strongly_connected_components(adj))

#threading.Thread(target=main).start()     
    
'''

Sample Inputs

4 4 1 2 4 1 2 3 3 1 
5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 
9 13 1 2 3 2 1 5 9 1 5 9 8 1 7 8 5 8 7 6 6 4 5 4 4 3 3 4 

'''