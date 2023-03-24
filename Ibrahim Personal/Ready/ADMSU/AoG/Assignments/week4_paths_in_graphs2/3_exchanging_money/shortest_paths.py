#Uses python3

#import sys

'''
Running Time is O(|V||E|) + O(E) (for marking Infinite Arbitrage) =~ O(|V||E|)
'''


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    dist = distance
    prev = [-1] * len(adj)
    dist[s] = 0
    
    # Running the Bellman's Ford Algo |V|-1 times
    for i in range(len(adj)-1):
        for u in range(len(adj)):
            for index, vertex in enumerate(adj[u]):
                if dist[vertex] > dist[u] + cost[u][index]:
                    dist[vertex] = dist[u] + cost[u][index]
                    prev[vertex] = u # This is not needed for this Algo
    
    # Now running the Bellman's Ford Vth time if there are any distance changes then it means there is an infinite arbiterage in that loop              
    for u in range(len(adj)):
        if dist[u] == float('inf'):
            reachable[u] = 1
        for index, vertex in enumerate(adj[u]):
            if dist[vertex] > dist[u] + cost[u][index]:
                dist[vertex] = dist[u] + cost[u][index]
                shortest[vertex] = 1
                for neighbors in (adj[vertex]): # immediately mark all the neigbors of the vertex on which infinite arbitrage is found
                    shortest[neighbors] = 1
    
# Note that in the previous case though even if we mark all the neighbors of the vertex which are on negative cycle we may also mark the start node 
# but start node can also point to some other nodes which needs to be marked for infinite arbitrage 
# This case gets missed in the previous Shortest[neighbors] loop as any later node may mark start node as infinite arbitrage
# Hence we have to run the shortest[neighbors] loop once more to mark all the neigbors of start node if start node is infinite arbitrage
    for u in range(len(adj)):
        for neighbors in (adj[u]):
            if shortest[u] == 1:
                shortest[neighbors] = 1
                
    distance = dist       
    return (reachable, shortest, distance)


if __name__ == '__main__':
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    data = list(map(int, input().split()))
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
#    distance = [10**19] * n
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [0] * n
    reachable, shortest, distance = shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 1:
            print('*')
        elif shortest[x] == 1:
            print('-')
        else:
            print(distance[x])

####################### Sample Inputs #################
'''

5 4 1 2 1 4 1 2 2 3 2 3 1 -5 4 
6 7 1 2 10 2 3 5 1 3 100 3 5 7 5 4 10 4 3 -18 6 1 -1 1 
4 4 1 2 -5 4 1 2 2 3 2 3 1 1 1
3 3 1 2 7 1 3 5 2 3 2 1
3 3 1 2 7 1 3 5 2 3 2 3
5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 5
3 2 1 2 -1 2 3 1 1 
5 7 1 2 10 2 3 5 1 3 100 3 5 7 5 4 10 4 3 -18 5 1 -1 1
3 5 1 2 5 2 1 10 2 3 7 3 2 -18 3 1 -1 1
6 7 1 2 10 2 3 5 1 3 100 3 5 7 5 4 10 4 3 -18 6 1 -1 3
4 5 1 2 1 2 3 1 3 1 -3 3 4 1 4 3 1 4

'''