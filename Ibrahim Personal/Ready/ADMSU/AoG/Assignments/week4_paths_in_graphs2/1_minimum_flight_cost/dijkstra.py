#Uses python3

#import sys
#import queue

'''
- Notice that Djikstra's Algo gives wrong answer for negative weights
Time Complexity - T(MakeQueue) + |V|.T(ExtractMin) + |E|.T(ChangePriority)
Hence for Array Implementation of ExtractMin, Time Complexity - O(|V| + |V|^2 + |E|) =~ O(|V|^2)
Hence for Binary Heap Implementation of ExtractMin, Time Complexity - O(|V| + |V|log|V| + |E|log|V|) =~ O(|V| + |E|log|V|)
'''


def ExtractMin(H):
    values_list = list(H.values())
    keys_list = list(H.keys())
    min_distance_element = min(values_list) 
    min_index = keys_list[values_list.index(min_distance_element)] #Extracting the index of min distance
    del(H[min_index]) # deleting min distance
    return (min_index)

def MakeQueue(dist):
    H = {index: distance for index, distance in enumerate(dist)} #using dictionary as it does not change the index upon deletion of an element
    return H

def ChangePriority(H, v, dist):
    H[v] = dist # updating the distance values in H

def distance(adj, cost, s, t):
    #write your code here
    dist = [1000000000] * len(adj)
    prev = [-1] * len(adj)
    dist[s] = 0
    
    H = MakeQueue(dist) # Index and Distance as keys
    
    while len(H) != 0:
        u = ExtractMin(H)
        if u == t: # returning as soon as target element is found
            if dist[u] == 1000000000:
                return -1 # returning -1 if the target node is not reachable
            return(dist[u]) # returning dist[u] as soon as target element is found
        for index, vertex in enumerate(adj[u]):
            if dist[vertex] > dist[u] + cost[u][index]:
                dist[vertex] = dist[u] + cost[u][index]
                prev[vertex] = u # This is not needed for this Algo
                ChangePriority(H, vertex, dist[vertex])
                

if __name__ == '__main__':
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))
#    data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
#    data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5]
    data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2]
#    data = [3, 3, 1, 2, 1, 1, 3, -5, 2, 3, 2, 1, 3]
#    data = [5, 7, 1, 2, 4, 1, 3, 3, 2, 3, -2, 3, 4, -3, 3, 5, 1, 4, 2, 4, 4, 5, 2, 1, 4]
    
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
    
    
    
####################### Sample Inputs #################
'''
4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3 
5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5 
3 3 1 2 7 1 3 5 2 3 2 3 2 

'''    
