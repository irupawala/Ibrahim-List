# python3
from collections import deque

class Flowgraph():
    
    def __init__(self, vertex_count, edge_count):
        self.Matrix = [[0]*vertex_count for x in range(vertex_count)] # Declaring v x v matrix for vertex count
        
    def bfs (self, s_t_path):
        q = deque()
        q.append([0, 200000]) # List with last element and minumum flow
        
        while(len(q) != 0):
             current_element = q.popleft()
             current_node = current_element[0]
             flow = current_element[1]
                     
             for next_node in range(len(s_t_path)):
                                  
                 if(s_t_path[next_node] == -1 and graph.Matrix[current_node][next_node]): # If node is not visited and min flow is not zero
                     s_t_path[next_node] = current_node # store current node as the parent to next node
                     new_flow = min(flow, graph.Matrix[current_node][next_node])
                     if(next_node == (len(s_t_path)-1)): # sink reached return the flow
                         return new_flow
                     q.append([next_node, new_flow])  
                     
        return 0
             
def read_data(): # Reading data in the same fashion as given in the starter file
    vertex_count, edge_count = map(int, input().split())
    graph = Flowgraph(vertex_count, edge_count)
    
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.Matrix[u-1][v-1] += capacity
        
    return graph

def max_flow():
    
    flow = 0
    max_s_t_flow = 200,000   # Considering 20000 as infinite
    
    while (max_s_t_flow != 0):
        
        s_t_path = [-1] * (len(graph.Matrix[0])) # s_t_path stores for each node it's parent
        s_t_path[0] = -2 # -2 in this path is source, has no parent
        
        max_s_t_flow = graph.bfs(s_t_path)
        
        if max_s_t_flow == 0: # If flow on the path is zero this means no extra flow can not be added, break loop and return flow which is maximum
            break
        
        flow += max_s_t_flow
        
        # to Update the residual capacity graph
        s_t_cur_node = len(s_t_path)-1 # starting from the last node        
        while(s_t_cur_node != 0): #  moving to source adding flow and creating residual graph
            prev_node = s_t_path[s_t_cur_node]
            graph.Matrix[prev_node][s_t_cur_node] -= max_s_t_flow # Reducing flow in backward path
            graph.Matrix[s_t_cur_node][prev_node] += max_s_t_flow # Adding flow in forward path
            s_t_cur_node = prev_node
            
    return flow                    

    

if __name__ == '__main__':
    
    graph = read_data()
    print(max_flow())



####################### Time & Space Complexity ###############################
    
# Time Complexity (runtime) = O(|E||f|)    
# Space Complexity = O(|V||E|^2)
    
# This code passes the grader to understand how it is implemented refer the explaination given in this video
    
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