#Uses python3
#import sys

'''
To Solve this problem apply BFS consequently marking Black and White Balls
If the connected node is same color return 0 immediately

Running Time of BFS is O(|V|+|E|)
'''


from collections import deque
from collections import namedtuple

node_detail = namedtuple("node_detail", ["index", "color"])

def bipartite(adj):
    #write your code here
    q = deque()
    black, white = set(), set()
    
    processed = [False] * len(adj)
    q.append(node_detail(0, "white")) 
    white.add(0)
    
    while len(q):
      node = q.popleft()
      processed[node.index] = True # Mark the node as processed
      
      if node.color == "white":          
          for x in adj[node.index]:
              if x in white: return 0 # If the connected node is same color return 0 immediately
              if not processed[x]: 
                  q.append(node_detail(x, "black"))
                  black.add(x)
      else:
          for x in adj[node.index]:
              if x in black: return 0 # If the connected node is same color return 0 immediately
              if not processed[x]:             
                  q.append(node_detail(x, "white"))
                  white.add(x)

    return 1

if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))
    
#    data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
#    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
#    data = [6, 4, 1, 2, 2, 3, 3, 4, 5, 6] #  if the graph is not fully connected, it's still a bipartite
#    data = [6, 7, 1, 2, 1, 4, 1, 6, 2, 3, 2, 5, 3, 4, 3, 6, 4, 5, 5, 4, 5, 6]
#    data = [6, 9, 1, 2, 1, 4, 1, 6, 2, 3, 2, 5, 3, 4, 3, 6, 4, 5, 5, 6]
    data = [8, 7, 5, 2, 4, 2, 3, 4, 1, 4, 6, 7, 7, 8, 8, 6]
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
