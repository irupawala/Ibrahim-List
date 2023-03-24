#Uses python3

#import sys
#import threading
#sys.setrecursionlimit(200000)

'''
- To Understand please watch the video - https://www.youtube.com/watch?v=TyWtx7q2D7Y
- To solve it each node is assigned a low-link value while exploring and then similar low-link value is assigned to the nodes present on Stack
- Time Complexity: The above algorithm mainly calls DFS, DFS takes O(V+E) for a graph represented using adjacency list. 
'''

class tarjans():
    
    def __init__(self, adj, n):
        self.id = 0 # Used to give each node and Id
        self.connected_comp = 0 # Used to count number of SCCs found

        # Index i in these arrays represents node i
        self.adj_list = adj
        self.ids = [-1 for x in range(n)] # -1 for UNVISITED, 
        # serves two purpose 1. to check ifVisted 2. to keep ids of node
        self.low = [0 for x in range(n)]
        self.onStack = [False for x in range(n)]    
        self.stack = []
        self.scc_list = []
    
        for i, x in enumerate(self.ids):
            if x == -1:
                self.dfs(i)
                
#        print(f"connected_comp = {self.connected_comp}")
#        print(f"scc_list = {self.scc_list}")
        print(self.connected_comp)
                
    def dfs(self,at_index):
        self.stack.append(at_index)
        self.onStack[at_index] = True 
        self.id += 1
        self.ids[at_index] = self.id
        self.low[at_index] = self.id
        
        # Visit all neighbors and min low-link on callback
        
        for to_index in self.adj_list[at_index]:
            if self.ids[to_index] == -1:
                self.dfs(to_index)
            if self.onStack[to_index]:
                self.low[at_index] = min(self.low[at_index], self.low[to_index])
                
        # After having visited all the neighbors of 'at_index'
        # If we're at the start of a SCC empty the stack 
        # untill we're back to the start of the SCC.

        if self.ids[at_index] == self.low[at_index]:
            scc = []
            for x in range(len(self.stack)):
                node = self.stack.pop(len(self.stack)-1)
                self.onStack[node] = False
                self.low[node] = self.ids[at_index]
                scc.append(node)
                if node == at_index:
                    self.scc_list.append(scc)
                    break
                
            self.connected_comp += 1


if __name__ == '__main__':
#def main():
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))    
    
    
#    data = list(map(int, input().split())) 
#    data = [9, 10, 1, 2, 2, 3, 3, 4, 4, 1, 3, 5, 5, 6, 6, 7, 7, 5, 8, 7, 8, 9]
#    data = [10, 15, 1, 2, 2, 3, 3, 10, 10, 1, 3, 1, 3, 4, 4, 5, 5, 6, 6, 4, 6, 3, 5, 7, 7, 8, 8, 9, 9, 5, 8, 5]
    
#    data = [8, 13, 1, 2, 2, 1, 1, 3, 3, 4, 2, 4, 5, 3, 4, 5, 5, 6, 4, 6, 5, 7, 7, 6, 6, 8, 8, 7]
    data = [8, 13, 1, 2, 2, 3, 3, 1, 5, 6, 6, 7, 7, 5, 6, 1, 7, 3, 7, 1, 4, 8, 8, 4, 4, 5, 8, 6]
#    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    tarjans(adj, n)
    
#threading.Thread(target=main).start()     