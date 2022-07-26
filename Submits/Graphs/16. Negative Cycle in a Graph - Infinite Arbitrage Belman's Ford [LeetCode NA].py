#Uses python3

# Coursera Data Structures and Algorithms - Algorithms of Graph, Weekk4, Problem 2 detecting_anomalies

'''
- Apply Bellman's Ford Algo |V|-1 times. If there are no negative cycles then all the nodes optimal
distance should've been calculated in |V|-1 cycles. If at |V| cycle too some distance is getting changed then surely there is a negative cycle

- Returns 1 if there is a negative cycle
'''

def negative_cycle(adj, cost):
    
    dist = [100000] * len(adj)
    dist[0] = 0
    
    for i in range(len(adj)-1):
        for u in range(len(adj)):
            for index, vertex in enumerate(adj[u]):
                if dist[vertex] > dist[u] + cost[u][index]:
                    dist[vertex] = dist[u] + cost[u][index]
                    
    for u in range(len(adj)):
        for index, vertex in enumerate(adj[u]):
            if dist[vertex] > dist[u] + cost[u][index]:
                return 1
            
    return 0


if __name__ == '__main__':

    data = list(map(int, input().split()))  
    # data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

####################### Sample Inputs #################
'''
4 4 1 2 -5 4 1 2 2 3 2 3 1 1
5 7 0 1 4 0 2 3 1 3 4 1 2 -2 2 3 -3 3 4 2 4 2 -3
4 4 1 2 1 4 1 2 2 3 2 1 3 5 
5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 
3 3 1 2 7 1 3 5 2 3 2 
'''

'''
Time Complexity - O(|V||E|)
'''
