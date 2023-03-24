# python3
from collections import deque

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity

class FlowGraph:

    def __init__(self, vertex_count, edge_count):
        # List of all - forward and backward - edges
        self.edges = []
        # This adjacency lists stores edges id of the edge originating from the node_index equal to corresponding list index
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.adjacency_list[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.adjacency_list[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.adjacency_list)

    def get_ids(self, from_):
        return self.adjacency_list[from_]

    def get_edge(self, id):
        return self.edges[id] 

    def add_flow(self, id, flow):
        self.edges[id].capacity -= flow
        k = id ^ 1
        self.edges[k].capacity += flow
        
    def bfs (self, s_t_path, s_t_path_edge_id):
        s_t_path_edge_id_initial = s_t_path_edge_id
        q = deque()
        q.append([0, float('inf')]) # queue with last element and minimum flow

        while(len(q) != 0):
            current_element = q.popleft()
            current_node = current_element[0]
            flow = current_element[1]
            
            outgoing_edges = self.get_ids(current_node)
            for edge_id in outgoing_edges:
                edge = self.get_edge(edge_id)
                capacity = edge.capacity
                next_node = edge.v
                
                if (s_t_path[next_node] == -1 and capacity > 0):
                    s_t_path[next_node] = current_node
                    s_t_path_edge_id[next_node] = edge_id
                    new_flow = min(flow, capacity)
                    if (next_node == vertex_count-1):
                        return new_flow, s_t_path_edge_id
                    q.append([next_node, new_flow])
        
        return 0, s_t_path_edge_id_initial               
        
def max_flow(vertex_count, edge_count):
    
    flow = 0
    max_s_t_flow = float('inf')  
    
    while (max_s_t_flow != 0):

        s_t_path = [-1] * (vertex_count) # s_t_path stores for each node it's parent
        s_t_path[0] = -2 # -2 in this path is source, has no parent
        s_t_path_edge_id = [-1] * (vertex_count)
        
        max_s_t_flow, s_t_path_edge_id = graph.bfs(s_t_path, s_t_path_edge_id)

        if max_s_t_flow == 0: # If flow on the path is zero this means no extra flow can not be added, break loop and return flow which is maximum
            break
        
        flow += max_s_t_flow 
        
        s_t_cur_node = len(s_t_path)-1
        while(s_t_cur_node != 0):
            prev_node = s_t_path[s_t_cur_node]
            prev_edge_id = s_t_path_edge_id[s_t_cur_node]
            graph.add_flow(prev_edge_id, max_s_t_flow)
            s_t_cur_node = prev_node 
            
    return flow              

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count, edge_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph, vertex_count, edge_count

if __name__ == '__main__':
    graph, vertex_count, edge_count = read_data()
    print(max_flow(vertex_count, edge_count))

####################### Time & Space Complexity ###############################
    
# Time Complexity (runtime) = O(|E||f|)    
# Space Complexity = O(|V||E|^2)
    
# https://www.youtube.com/watch?v=_aWooet7O_4    
    
###############################################################################
    

'''

Sample Test Cases and Ansers:
   
4 5 
1 2 10
1 3 10
2 3 1
3 4 10
2 4 10   
Ans - 20    
    
4 5 
1 2 1000
1 3 1000
2 3 1
3 4 1000
2 4 1000
Ans - 2000

4 5 
1 2 5
1 3 7
2 4 10
3 2 3
3 4 5
Ans - 12

4 5 
1 2 2
1 3 4
2 4 1
3 4 5
2 3 3 
Ans - 6

2 4
1 1 10
1 2 1
1 2 4
2 1 9

6 6 
1 2 10
2 3 10
3 5 7
5 4 5
4 2 5
5 6 15 
Ans - 7  
 
6 6 
1 2 7
1 3 8
1 6 10
6 3 2 
6 2 11
3 5 12
Ans - 10

6 10
1 2 7
1 3 8
1 6 10
6 3 2 
6 2 11
3 5 12
6 5 5
2 5 1
5 4 14
2 4 21
Ans - 10

6 10
1 2 7
1 3 8
1 4 10
4 3 2
4 2 11
4 5 5 
3 5 12
2 5 1
5 6 14
2 6 21
Ans - 25
 
6 9
1 2 16
1 3 13
3 2 4
2 4 12
4 3 9
3 5 14
5 4 7
4 6 20
5 6 4
Ans - 23

6 9
1 2 10
1 3 20
3 5 33
3 4 20
2 5 10
2 4 50
4 5 20
5 6 1
4 6 2
Ans - 3

6 10
1 3 1
1 2 38
2 3 8
2 4 10
3 4 26
2 5 13
5 3 2
4 5 20
4 6 8
5 6 1
Ans - 9

8 16
1 2 38
1 7 2
1 3 1
2 3 8
2 4 10
3 4 26
4 7 24
2 5 13
5 3 2
4 5 20
4 7 24
7 8 27
4 8 1
4 6 8
5 6 1
5 8 7
Ans - 30

8 16
1 7 2 
1 2 38
1 3 1
2 3 8
3 4 26
2 4 10
4 7 24
2 5 13
5 3 2
4 5 20
8 7 27
5 6 1
4 6 8
4 8 1
5 8 7 
6 8 7
Ans - 15

6 10
1 2 38
1 3 1
2 3 8
3 4 26
2 4 10
2 5 13
5 3 2
4 5 20
5 6 1
4 6 8
Ans - 9

6 9 
1 2 16
1 3 13
3 2 4
2 4 12
4 3 9
3 5 14
5 4 7
4 6 20
5 6 4
Ans - 23

8 16
1 2 38
1 3 1
2 3 8
1 7 2
2 4 10
3 4 26
4 7 24
2 5 13
5 3 2
4 5 20
7 8 27
4 6 8
5 6 1
5 8 7
6 8 7
4 6 8
Ans - 31

4 5 
1 2 8
1 3 8
3 2 1
3 4 8
2 4 8 
Ans - 16

2 5 
1 1 10000
1 2 1
1 2 4
1 2 100
2 1 900
Ans - 105

6 9
1 2 7 
2 3 5 
2 4 3 
4 3 3
5 2 3
5 4 2 
1 5 4 
4 6 5
3 6 8 

  
'''