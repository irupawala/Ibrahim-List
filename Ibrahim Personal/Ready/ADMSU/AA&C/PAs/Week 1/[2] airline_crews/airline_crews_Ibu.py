# python3
from collections import deque

class Flowgraph():
    
    def __init__(self, flights, crews):
        self.flights = flights
        self.crews = crews
        self.matrix_size = self.flights + self.crews + 2 # 1 for source and 1 for sink
        self.crews_assigned = [-1] * self.matrix_size
        self.sink = self.flights + self.crews + 1
#        self.Matrix = [[0]*self.matrix_size for _ in range(self.matrix_size)]
        self.Matrix = {j:{i:0 for i in range(self.matrix_size)} for j in range(self.matrix_size)} # creating dictionary instead of list so that indexing key is easy
        
    def bfs (self, s_t_path):
        q = deque()
        q.append([0, 200000])
        
        while(len(q) != 0):
             current_element = q.popleft()
             current_node = current_element[0]
             flow = current_element[1]
                     
             for next_node in range(len(s_t_path)): # 
                                  
                 if(s_t_path[next_node] == -1 and graph.Matrix[current_node][next_node]): # copied from edmonds karp
                     s_t_path[next_node] = current_node
                     new_flow = min(flow, graph.Matrix[current_node][next_node])
                     if(next_node == (len(s_t_path)-1)):
                         return new_flow
                     q.append([next_node, new_flow])     
                     
        return 0
    
    
def bipartite():
    
    max_s_t_flow = 200000   
    crew_assigned = [-1] * graph.flights
    
    while (max_s_t_flow != 0):
        
        s_t_path = [-1] * (len(graph.Matrix[0]))
        s_t_path[0] = -2
        
        max_s_t_flow = graph.bfs(s_t_path)
        
        if max_s_t_flow == 0:
            break
        
        s_t_cur_node = len(s_t_path)-1
        
        while(s_t_cur_node != 0): # start from sink and keep on modifying till source
            prev_node = s_t_path[s_t_cur_node]
            graph.Matrix[prev_node][s_t_cur_node] -= max_s_t_flow
            graph.Matrix[s_t_cur_node][prev_node] += max_s_t_flow
            s_t_cur_node = prev_node
            
            
    for (crew_k,crew_v) in graph.Matrix[graph.sink].items(): # After the Matrix is modified with all the flows possible navigate to find where flow exixsts
        if crew_v == 1: # If value is 1 then we have to find crew_no from key but note that we have first added flights
            crew_no = crew_k - graph.flights # To get the crew no from matrix index
            for (flight_k,flight_v) in graph.Matrix[crew_k].items(): 
                if flight_v == 1:
                    crew_assigned[flight_k-1] = crew_no # Assigning crew_no to respective flight index
                    
    return crew_assigned
    
             
def read_data():
    flights, crews = map(int, input().split())
    graph = Flowgraph(flights, crews)
    source = 0
    sink = flights + crews + 1 # Creating a matrix with all the elements from flights and crew 
    
    for i in range(flights):
#       crews_i = map(int, input().split())
       crews_i = [int(capacity) for capacity in input().split()] # Creating a list of crew members availability for that flight
       
       for j in range(crews):           
           graph.Matrix[source][i+1] = 1 # capacity from source to flights is 1 for bipartite
           graph.Matrix[i+1][j+flights+1] = crews_i[j] # capacity from flights to crew
           graph.Matrix[j+flights+1][sink] = 1 # capacity from flight to sink is 1 for bipartite 
            
    return graph


if __name__ == '__main__':    
    graph = read_data()
    crews_list = bipartite()
    
    for x in crews_list:
        print(x, end=' ')
