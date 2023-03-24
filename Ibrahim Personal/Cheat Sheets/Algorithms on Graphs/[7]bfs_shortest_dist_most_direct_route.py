#Uses python3

#import sys
#import queue

'''
Running Time of BFS is O(|V|+|E|)
'''

class queue():
    def __init__(self):
        self.queue = []
        self.queue_len = 0
        
    def enqueue(self, element):
        self.queue.append(element)
        self.queue_len += 1
        
    def dequeue(self):
        self.queue_len -= 1
        return(self.queue.pop(0))
    
    def queue_length(self):
        return (self.queue_len)
        

def distance(adj, s, t):
    #write your code here
    
    dist = [-1] * len(adj)
    prev = [-1] * len(adj)
    dist[s] = 0
    
    q = queue()
    q.enqueue(s)
    
    while(q.queue_length() != 0):
        u = q.dequeue()
        if u == t:
            return(dist[u])
        for vertex in adj[u]:
            if dist[vertex] == -1:
                q.enqueue(vertex)
                dist[vertex] = dist[u] + 1
                prev[vertex] = u
                
                
    return(dist[t])
                
if __name__ == '__main__':
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
#    data = list(map(int, input().split()))
    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
#    data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5]
#    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))


####################################################################
"""

Sample Inputs

4 4 1 2 4 1 2 3 3 1 2 4 
5 4 5 2 1 3 3 4 1 4 3 5 
5 7 2 1 3 2 3 1 4 3 4 1 5 2 5 3 4 2

"""