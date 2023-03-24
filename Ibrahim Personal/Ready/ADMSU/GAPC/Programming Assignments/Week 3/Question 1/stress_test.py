# python3
from collections import deque
import queue
import random

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
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].diff -= flow
        self.edges[id ^ 1].diff += flow
                    
    def bfs (self, s_t_path, s_t_path_edge_id, source, sink):
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
    
    
    def max_flow(self, vertex_count, edge_count):
        
        source = vertex_count 
        sink = vertex_count + 1
        flow = 0
        max_s_t_flow = float('inf')  
        s_t_path_edge_id_last = set()
        
        while (max_s_t_flow != 0):
            
            s_t_path = [-1] * (vertex_count + 2) # s_t_path stores for each node it's parent
            s_t_path[source] = -2 # -2 in this path is source, has no parent
            s_t_path_edge_id = [-1] * (vertex_count + 2)        
            
            max_s_t_flow, s_t_path_edge_id = self.bfs(s_t_path, s_t_path_edge_id, source, sink)
            
            if max_s_t_flow == 0: # If flow on the path is zero this means no extra flow can not be added, break loop and return flow which is maximum
                break                
    
            flow += max_s_t_flow     
            s_t_cur_node = len(s_t_path)-1
            
            while(s_t_cur_node != source):
                prev_node = s_t_path[s_t_cur_node]
                prev_edge_id = s_t_path_edge_id[s_t_cur_node]
                s_t_path_edge_id_last.add(prev_edge_id)
                self.add_flow(prev_edge_id, max_s_t_flow)
                s_t_cur_node = prev_node 
      
        return flow  
    
    def findCirculation(self, vertex_count, edge_count, total_demand):
        flow = self.max_flow(vertex_count, edge_count)
        flows = [0] * edge_count
        if flow != self.total_demand:
            return False, flows
        else:
            for i in range(edge_count):
                forward_edge = self.edges[i * 2]
                flows[i] = forward_edge.flow + forward_edge.lower_bound
            return True, flows
                
    def readOutput(self, flow, flows):
        if not flow:
            print('NO')
        else:
            print('YES')
            print('\n'.join(map(str, flows)))
            
            
    def readOutput_list(self, flow, flows):
        if not flow:
            ANS = 'NO'
        else:
            ANS = 'YES'              
        return ANS, flows 

     
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
                                
    return graph, vertex_count, edge_count, graph.total_demand


def read_data_list(vertex_count, edge_count, edges):
    vertex_count, edge_count = vertex_count, edge_count
    graph = FlowGraph(vertex_count, edge_count)
    for e in edges:
        u = int(e[0])
        v = int(e[1])
        lower_bound = int(e[2])
        capacity = int(e[3])
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
                                
    return graph, vertex_count, edge_count, graph.total_demand


def CirculationProblem(vertex_count, edge_count, edges):
    graph, vertex_count, edge_count, total_demand = read_data_list(vertex_count, edge_count, edges)
    flow, flows = graph.findCirculation(vertex_count, edge_count, total_demand)
    return graph.readOutput_list(flow, flows)    

#################################################################################################################################################################################
                

class Edge_SOLN:
    def __init__( self, u, v, lower_bound, capacity ):
        self.u = u
        self.v = v
        self.lower_bound = lower_bound
        self.capacity = capacity
        self.diff = capacity - lower_bound
        self.flow = 0

class FlowGraph_SOLN:

    def __init__( self, n ):
        self.edges = []
        self.graph = [[] for _ in range(n + 2)]
        self.dv = [0] * (n + 2)
        self.DD = 0

    def add_edge_SOLN( self, from_, to, lower_bound, capacity ):
        forward_edge = Edge_SOLN(from_, to, lower_bound, capacity)
        backward_edge = Edge_SOLN(to, from_, 0, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        self.dv[from_] += lower_bound
        self.dv[to] -= lower_bound


    def construct_flow_SOLN( self, id, flow ):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].diff -= flow
        self.edges[id ^ 1].diff += flow

    def get_ids_SOLN( self, from_ ):
        return self.graph[from_]


    def size_SOLN( self ):
        return len(self.graph)

    def get_edge_SOLN( self, id ):
        return self.edges[id]

    def bfs_SOLN( self, graph, from_, to ):
        X = float('inf')
        hasPath = False
        n = graph.size_SOLN()
        dist = [float('inf')] * n
        path = []
        parent = [(None, None)] * n
        q = queue.Queue()
        dist[from_] = 0
        q.put(from_)
        while not q.empty():
            currFromNode = q.get()
            for id in graph.get_ids_SOLN(currFromNode):
                currEdge = graph.get_edge_SOLN(id)
                if float('inf') == dist[currEdge.v] and currEdge.diff > 0:
                    dist[currEdge.v] = dist[currFromNode] + 1
                    parent[currEdge.v] = (currFromNode, id)
                    q.put(currEdge.v)
                    if currEdge.v == to:
                        while True:
                            path.insert(0, id)
                            currX = graph.get_edge_SOLN(id).diff
                            X = min(currX, X)
                            if currFromNode == from_:
                                break
                            currFromNode, id = parent[currFromNode]
                        hasPath = True
                        return hasPath, path, X
        return hasPath, path, X

    def max_flow_SOLN( self, graph, from_, to ):
        flow = 0
        while True:
            hasPath, path, X = self.bfs_SOLN(graph, from_, to)
            if not hasPath:
                return flow
            for id in path:
                graph.construct_flow_SOLN(id, X)
            flow += X
        return flow

    def find_Circulation_SOLN( self, graph, n, m ):
        flow = self.max_flow_SOLN(graph, n, n + 1)
        flows = [0] * m
        if flow != graph.DD:
            return False, flows
        else:
            for i in range(m):
                forward_edge = graph.edges[i * 2]
                flows[i] = forward_edge.flow + forward_edge.lower_bound
            return True, flows

#    def write_SOLN( self, flow, flows ):
#        if not flow:
#            print('NO')
#        else:
#            print('YES')
#            print('\n'.join(map(str, flows)))                
                
    def write_SOLN( self, flow, flows ):
        if not flow:
            ANS = 'NO'
        else:
            ANS = 'YES'              
        return ANS, flows    
    
def _input(vertex_count, edge_count, edges):
    vertex_count, edge_count = vertex_count, edge_count
    graph = FlowGraph_SOLN (vertex_count)
#        for _ in range(edge_count):
#            u, v, lower_bound, capacity = map(int, input().split())
#            graph.add_edge_SOLN(u - 1, v - 1, lower_bound, capacity)
        
    for e in edges:
        u = int(e[0])
        v = int(e[1])
        lower_bound = int(e[2])
        capacity = int(e[3])
        graph.add_edge_SOLN(u - 1, v - 1, lower_bound, capacity)    
        
    for v in range(vertex_count):
        if graph.dv[v] < 0:
            graph.add_edge_SOLN(vertex_count, v, 0, -graph.dv[v])
        if graph.dv[v] > 0:
            graph.add_edge_SOLN(v, vertex_count + 1, 0, graph.dv[v])
            graph.DD += graph.dv[v]

    return graph, vertex_count, edge_count    

def CirculationProblem_METHOD(vertex_count, edge_count, edges):
    graph, vertex_count, edge_count = _input(vertex_count, edge_count, edges)
    flow, flows = graph.find_Circulation_SOLN(graph, vertex_count, edge_count)
    return graph.write_SOLN(flow, flows)    


##############################################################################################################################


def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def stress_test():
    while(1):
        print("-----------------------------------------------------------")
        vertex_count = random.randint(2, 4)
        edge_count = random.randint(vertex_count-1, 6)
#        print(vertex_count)
#        print(edge_count)
        edges = []
        first_node_list = random.sample(range(1, vertex_count+1), vertex_count)
        print(first_node_list)

        
        for edge in range(edge_count):
            first_node_list = random.sample(range(1, vertex_count+1), vertex_count)
            first_node = random.choice(first_node_list)
            second_node = random.choice(first_node_list)
            if second_node == first_node:
                first_node_list.remove(first_node)
                second_node = random.choice(first_node_list)
                first_node_list.append(first_node)
            lower_bound = random.randint(0, 10)
            capacity = lower_bound + random.randint(0, 5)
            edge = [first_node, second_node, lower_bound, capacity]
            edges.append(edge)
            first_node_list.remove(first_node)
            
        print(vertex_count)
        print(edge_count)
        print(edges)
        
        ibru_result_ANS,  ibru_result_flows = CirculationProblem(vertex_count, edge_count, edges)
        solution_result_ANS, solution_result_flows = CirculationProblem_METHOD(vertex_count, edge_count, edges)

        if ((ibru_result_ANS != solution_result_ANS) or Diff(ibru_result_flows, solution_result_flows) != []):
            break
        else:
            print(ibru_result_ANS)
            print(ibru_result_flows)
        

if __name__ == '__main__':
    stress_test()


'''

This stress test compares codes developed by me with the solution

'''
