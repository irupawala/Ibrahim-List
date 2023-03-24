# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        k = id ^ 1
        self.edges[k].flow -= flow
        
        
def PreOrderTraversal(graph, from_, to, s_t_path, s_t_path_flows, s_t_found): # Depth First Search Traversal as it is Ford-Fulkerson's Algorithm
    
    neighbor_vertice = graph.get_ids(from_)
    
    for vertice in neighbor_vertice:
        edge = graph.get_edge(vertice)
        
        if vertice % 2 == 0: # meaning the edge is forward edge   
            flow = edge.capacity - edge.flow
        else:
            flow = -(edge.flow) # meaning the edge is reverse edge  
        
        if flow > 0:
            if edge.v not in s_t_path: # append flow and node to s_t_path if it does not exists
                s_t_path_flows.append(flow)
                s_t_path.append(edge.v)
                
                if edge.v == to: # If sink is reached then return        
                    s_t_found = True
                    return(s_t_path, s_t_path_flows, s_t_found)
                
                if edge.v != to:
                    s_t_path, s_t_path_flows, s_t_found = PreOrderTraversal(graph, edge.v, to, s_t_path, s_t_path_flows, s_t_found)
                    if s_t_found == True: # Return is path has been reached in some deeper recursive iteration 
                        return(s_t_path, s_t_path_flows, s_t_found)
                    else: 
                        s_t_path.pop() # remove node if not the next node
                        s_t_path_flows.pop()                                              

    return(s_t_path, s_t_path_flows, s_t_found)


def find_path(graph, from_, to):
    s_t_path = [from_] # Creating a path from u to v with starting from u. If the path exists !!
    s_t_path_flows = [] # Creating a list to keep track of all the flow values in each of the path
    s_t_found = False # using a Flag, as soon as path is found from u to v this Flag will be turned False and results will be returned
    
    s_t_path, s_t_path_flows, s_t_found = PreOrderTraversal(graph, from_, to, s_t_path, s_t_path_flows, s_t_found)
    
    if s_t_found == True: # Path found
        max_flow = min(s_t_path_flows) # min flow from some node to the next node in the entire path is the MAX flow which will flow through u to v path
        return (s_t_path, max_flow)
        
    return([], 0)
    

def Residual_graph(graph, s_t_path, X):
    len_s_t_path = len(s_t_path)
    
    for x in range(len_s_t_path):
        
        if x == len_s_t_path - 1: # end of the path reached
            return
        
        u = s_t_path[x]
        v = s_t_path[x+1]        
        neighbor_vertice = graph.get_ids(u) # gives adjacency list of that vertice
        
        for vertice in neighbor_vertice:
            edge = graph.get_edge(vertice) # get.edge returns an object having details (variables) like next node, previous node, max_flow and capacity           
            if vertice % 2 == 0:
                flow = edge.capacity - edge.flow # objects are created such that even vertice contains flow in direction from source to sink
            else:
                flow = -(edge.flow) # odd vertices contains -ve flows in direction from sink to source
                
            if flow > 0:                            
                if v == edge.v: # if the next node in the s_t_path is also the next node of the current node
                    if edge.v in s_t_path: # If next node of the current node is in the list of s_t_path
                        graph.add_flow(vertice, X)
                        break

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def max_flow(graph, from_, to):
    flow = 0
    s_t_path = [1] # so that while loop condition is True initially and code enters while loop
      
    while s_t_path != []:
        s_t_path, X = find_path(graph, from_, to) # X is the max flow in this iteration
#        print(s_t_path, X)
        Residual_graph(graph, s_t_path, X) # Modifying the original graph to residual graph to find new flow on it
        flow += X # Adding max flow from the retuned path to Total flow
        
    return flow
    

if __name__ == '__main__':
    graph = read_data()  # Reading the data first. This code is given in the starter file
    print(max_flow(graph, 0, graph.size() - 1)) # Calling max_flow to find the maximum flow


####################### Time & Space Complexity ###############################
    
# Time Complexity (runtime) = O(|E||f|)    
# Space Complexity = ?
    
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
1 2 2
1 3 4
2 4 1
3 4 5
2 3 3 
Ans - 6

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


  
'''