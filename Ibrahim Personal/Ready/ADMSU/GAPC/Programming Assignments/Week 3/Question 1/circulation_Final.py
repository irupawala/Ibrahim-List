# python3
from collections import deque

class Edge:

    def __init__(self, u, v, lower_bound, capacity):
        self.u = u
        self.v = v
        self.lower_bound = lower_bound
        self.capacity = capacity
        self.diff = capacity - lower_bound
        self.flow = 0
        
class Nodes:
    
    def __init__(self, neighbors, demand):
        self.neighbors = neighbors
        self.demand = demand

class FlowGraph:

    def __init__(self, vertex_count, edge_count):
        # List of all - forward and backward - edges
        self.edges = []
        # This adjacency lists stores edges id of the edge originating from the node_index equal to corresponding list index
        self.adjacency_list = [Nodes([], 0) for _ in range(vertex_count + 2)] # +2 for source and sink
        self.total_demand = 0

    def add_edge(self, from_, to, lower_bound, capacity):
        forward_edge = Edge(from_, to, lower_bound, capacity)
        backward_edge = Edge(to, from_, 0, 0)
        self.adjacency_list[from_].neighbors.append(len(self.edges))
        self.adjacency_list[from_].demand -= lower_bound # generating flow of lower bounds f0(u, v) = l(u,v)
        self.edges.append(forward_edge)
        self.adjacency_list[to].neighbors.append(len(self.edges))
        self.adjacency_list[to].demand += lower_bound # generating flow of lower bounds f0(u, v) = l(u,v)
        self.edges.append(backward_edge)

    def get_ids(self, from_):
        return self.adjacency_list[from_].neighbors

    def get_edge(self, id):
        return self.edges[id] 

    def add_flow(self, id, flow):
        self.edges[id].diff -= flow
        self.edges[id].flow += flow
        k = id ^ 1
        self.edges[k].diff += flow
        self.edges[k].flow -= flow        
                    
    def bfs (self, s_t_path, s_t_path_edge_id, source, sink):
#        print(f"Source = {source}")
#        print(f"Sink = {sink}")
        s_t_path_edge_id_initial = s_t_path_edge_id
        q = deque()
        q.append([source, float('inf')]) # starting the max flow from source queue with last element and minimum flow
        
        while(len(q) != 0):
            current_element = q.popleft()
            current_node = current_element[0]
            flow = current_element[1]
            outgoing_edges = self.get_ids(current_node)
#            print(f"outgoing_edges = {outgoing_edges}")

            for edge_id in outgoing_edges:
                edge = self.get_edge(edge_id)
                diff, next_node = edge.diff, edge.v
                
                if (s_t_path[next_node] == -1 and diff > 0):
                    s_t_path[next_node] = current_node
                    s_t_path_edge_id[next_node] = edge_id
                    new_flow = min(flow, diff)
                    if (next_node == sink):
                        return new_flow, s_t_path_edge_id
                    q.append([next_node, new_flow])
                    
        return 0, s_t_path_edge_id_initial       

def max_flow(vertex_count, edge_count):

    source = vertex_count 
    sink = vertex_count + 1
    flow = 0
    max_s_t_flow = float('inf')  
    
    while (max_s_t_flow != 0):
        
        s_t_path = [-1] * (vertex_count + 2) # s_t_path stores for each node it's parent
        s_t_path[source] = -2 # -2 in this path is source, has no parent
        s_t_path_edge_id = [-1] * (vertex_count + 2)        
        
        max_s_t_flow, s_t_path_edge_id = graph.bfs(s_t_path, s_t_path_edge_id, source, sink)
#        print(f"max_s_t_flow = {max_s_t_flow}")
        
        if max_s_t_flow == 0: # If flow on the path is zero this means no extra flow can not be added, break loop and return flow which is maximum
            break                

        flow += max_s_t_flow     
        s_t_cur_node = len(s_t_path)-1
        
#        print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Before Assignment xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#        for i in range(len(graph.edges)):
#                if i%2 == 0:
#                    print(f"------------------------------------------------edge_id = {i}")
#                    print(f"from = {graph.edges[i].u}, to = {graph.edges[i].v}, capacity = {graph.edges[i].capacity}, lower_bound = {graph.edges[i].lower_bound}, diff = {graph.edges[i].diff}, flow = {graph.edges[i].flow}")             
#        print(f"s_t_path = {s_t_path}")
#        print(f"s_t_path_edge_id = {s_t_path_edge_id}")
        
        while(s_t_cur_node != source):
            prev_node = s_t_path[s_t_cur_node]
            prev_edge_id = s_t_path_edge_id[s_t_cur_node]
            graph.add_flow(prev_edge_id, max_s_t_flow)
            s_t_cur_node = prev_node 
        
#        print(f"flow = {max_s_t_flow}")
#        print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx After Assignment xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#        for i in range(len(graph.edges)):
#                if i%2 == 0:
#                    print(f"------------------------------------------------edge_id = {i}")
#                    print(f"from = {graph.edges[i].u}, to = {graph.edges[i].v}, capacity = {graph.edges[i].capacity}, lower_bound = {graph.edges[i].lower_bound}, diff = {graph.edges[i].diff}, flow = {graph.edges[i].flow}")        
#              
    return flow

def findCirculation(vertex_count, edge_count):
    flow = max_flow(vertex_count, edge_count)
#    print(f"flow = {flow}")
    flows = [0] * edge_count
    if flow != graph.total_demand:
        return False, flows
    else:
        for i in range(edge_count):
            forward_edge = graph.edges[i * 2]
            flows[i] = forward_edge.flow + forward_edge.lower_bound
        return True, flows
    
    	                                       
def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count, edge_count)
    for _ in range(edge_count):
        u, v, lower_bound, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, lower_bound, capacity)  
    
    # Converting the graph with no demands and super source/sink
    source = vertex_count
    sink = vertex_count + 1
    
    for i in range(vertex_count):
        vertex = graph.adjacency_list[i]
        dv = 0 # demand constraints of original plot
        adjusted_demand = dv - vertex.demand # adjusted_demand = dv (0) - Lv
        
        if adjusted_demand < 0: # Source node vertex_count - 2                     
            graph.add_edge(source, i, 0, 0 - adjusted_demand)
            graph.total_demand += vertex.demand                    
        if adjusted_demand > 0: # Sink node vertex_count - 1  
            graph.add_edge(i, sink, 0, adjusted_demand)

#    print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#    for i in range(len(graph.edges)):
#            if i%2 == 0:
#                print(f"------------------------------------------------edge_id = {i}")
#                print(f"from = {graph.edges[i].u}, to = {graph.edges[i].v}, capacity = {graph.edges[i].capacity}, lower_bound = {graph.edges[i].lower_bound}, diff = {graph.edges[i].diff}, flow = {graph.edges[i].flow}")                                       
#    
    return graph, vertex_count, edge_count


def readOutput(flow, flows):
    if not flow:
        print('NO')
    else:
        print('YES')
        print('\n'.join(map(str, flows)))


if __name__ == '__main__':
    
    graph, vertex_count, edge_count = read_data()
    flow, flows = findCirculation(vertex_count, edge_count)
    readOutput(flow, flows)
    
'''

Executes the algorithm mentioned in lect17-flow-circ.pdf in the Material folder 

Note that this is a circulation Problem hence we have to just check two conditions for each vertex

1. le < fe < ce
2. flow_in = flow_out

- Max Flow Algorithm is invoked to check if maximum flow is equal to total demand if yes then circulation exists and we output
lower_bound + flow for each edge.

- diff is adjusted capacity meaning (capacity - lower_bound) amount of flow can only be further added to this edge. Thus we are assigning
lower_bound amount of flow to the graph from the start

- graphs with total_demand = 0 are difficult to understad because there will be no source/sink in this case but remember that in 
circulation problem there is no source that produces a flow and there is no sink that absorbs a flow. For this reason, we don not 
maximize flow in this problem, instead Max Flow algorithm (with source sink) comes to play only when there is some total demand.
Thus in the case when total_demand = sum of lower_bounds = 0, and hence Max_flow is also 0 thus satisfying circulation criteria 

'''