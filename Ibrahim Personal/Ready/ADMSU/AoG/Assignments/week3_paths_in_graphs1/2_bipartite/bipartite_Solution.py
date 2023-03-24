#Uses python3
import sys

'''
To Solve this problem apply BFS consequently marking Black and White Balls
If the connected node is same color return 0 immediately

Running Time of BFS is O(|V|+|E|)
'''


from collections import deque


def isBipartite(n, adj):
    dist = [float('inf')] * (n + 1)
    queue = deque()
    queue.append(1)
    dist[1] = 0
    while queue:
        now = queue.popleft()
        for v in adj[now]:
            if dist[v] == float('inf'):
                queue.append(v)
                dist[v] = dist[now] + 1
            else:
                if (dist[now] - dist[v]) % 2 == 0:
                    return 0
    return 1


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    adjacency_list = [[] for _ in range(n_vertices + 1)]
    for i in range(n_edges):
        a, b = map(int, input().split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    is_bipartite = isBipartite(n_vertices, adjacency_list)
    print(is_bipartite)