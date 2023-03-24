#Uses python3

import sys
#import queue

def ExtractMin(H):
    min_distance_element = min(H, key=lambda x: x[1])
    H.remove(min_distance_element)
    min_index = min_distance_element[0]
    return (min_index)

def MakeQueue(dist):
    dist_index = [_ for _ in range(len(dist))]
    H = [list(a) for a in zip(dist_index, dist)]
    return H

def ChangePriority(H, v, dist):
    index_list = list(map(lambda x: x[0], H))
    index_of_v = index_list.index(v)
    H[index_of_v][1] = dist

def distance(adj, cost, s, t):
    #write your code here
    dist = [1000000000] * len(adj)
    prev = [-1] * len(adj)
    dist[s] = 0
    
    H = MakeQueue(dist) # Index and Distance as keys
    
    while len(H) != 0:
        u = ExtractMin(H)
        if u == t:
            if dist[u] == 1000000000:
                return -1
            return(dist[u])
        for index, vertex in enumerate(adj[u]):
            if dist[vertex] > dist[u] + cost[u][index]:
                dist[vertex] = dist[u] + cost[u][index]
                prev[vertex] = u
                ChangePriority(H, vertex, dist[vertex])
                

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
