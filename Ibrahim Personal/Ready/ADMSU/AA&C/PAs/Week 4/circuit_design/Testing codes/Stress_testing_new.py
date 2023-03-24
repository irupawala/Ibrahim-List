import random
# python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

def post_order_to_index_convert(post_order):   
    sorted_by_values_dict = dict(sorted(post_order.items(), key=lambda x: x[1], reverse=True))
    post_order_vertex = list(sorted_by_values_dict.keys())
#    print(f"post_order_vertex = {post_order_vertex}")
    return(post_order_vertex)          
    
def explore_post_order(adj_list, visited, post_order, n, clock):
    visited[n] = True
    clock  = clock + 1 # to mark previsit 
    for x in adj_list[n]:
        if visited[x] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, x, clock)
    clock  = clock + 1        
    post_order[n] = clock
    return clock, post_order

def dfs_post_order(adj_list):
#    print(f"adj_list = {adj_list}")
    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()}
    connected_comp, clock = 0, 0
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
            connected_comp = connected_comp + 1
    
#    print(f"post_order = {post_order}, connected_comp = {connected_comp}")
    return post_order, connected_comp

def explore_connected_components(adj_list, visited, post_order, n, clock, scc):
    visited[n] = True
    clock  = clock + 1 # to mark previsit 
    scc.append(n)
    for x in adj_list[n]:
        if visited[x] == False:
            clock, post_order, scc = explore_connected_components(adj_list, visited, post_order, x, clock, scc)
    clock  = clock + 1        
    post_order[n] = clock
    return clock, post_order, scc

def dfs_connected_components(adj_list, post_order_vertex):   
    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()} 
    connected_comp, clock, scc_list = 0, 0, []

    for x in post_order_vertex:
        scc = []
        if visited[x] == False:
            clock, post_order, scc = explore_connected_components(adj_list, visited, post_order, x, clock, scc)
            connected_comp = connected_comp + 1
            scc_list.append(scc) 
        
    return post_order, connected_comp, scc_list

def number_of_strongly_connected_components(adj, adjr): 
    post_order_adjr, connected_comp_adjr = dfs_post_order(adjr)
    post_order_vertex = post_order_to_index_convert(post_order_adjr)
    post_order_adj, connected_comp_adj, scc_list = dfs_connected_components(adj, post_order_vertex)
#    print(f"scc_list = {scc_list}")
    return(scc_list)
    
def implicationGraph(n, clauses):

    adj, adjr  = {}, {}
    for n in range(1,n+1):
#        adj[n], adj[-n] = [], []
#        adjr[n], adjr[-n] = [], []
        
        adj[-n], adj[n] = [], []
        adjr[-n], adjr[n] = [], []        


    for x in clauses:
        if len(x) == 2: # For each 2-Clause
            l1 = x[0]
            l2 = x[1]            
            # -l1 --> l2
            adj[-l1].append(l2)
            adjr[l2].append(-l1)              
            # -l2 --> l1
            adj[-l2].append(l1)
            adjr[l1].append(-l2)    
        
        if len(x) == 1:
           l1 = x[0]
           adj[-l1].append(l1) 
           adjr[l1].append(-l1)
    
#    print(f"adj = {adj}")
#    print(f"adjr = {adjr}")
    return adj, adjr
    
def SAT_2_CNF(n, clauses):
    
    adj, adjr = implicationGraph(n, clauses)
    scc_list = number_of_strongly_connected_components(adj, adjr)    
#    print(f"scc_list = {scc_list}")    
    for x in range(1,n+1):
        for scc in scc_list:
            if ((x in scc) and (-x in scc)):
                return None
                
    literals = {n:None for n in  range(1, n+1)}
    for scc in scc_list:
        for literal in scc:            
            index = abs(literal)
            if literals[index] == None:
                literals[literal] = 0
                literals[-literal] = 1

    
    result = list(literals.values())
    result_list = [-i-1 if result[i] else i+1 for i in range(n)]
    return (result_list)

'''
if __name__ == "__main__":
#def main():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
#    n, m = 3, 3    
#    clauses = [(1, -3), (-1, 2), (-2, -3)]
    result = SAT_2_CNF(n, clauses)
#    print(f"result = {result}")

    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        result_list = [-i-1 if result[i] else i+1 for i in range(n)]
        print(" ".join(map(str, result_list)))
        
#threading.Thread(target=main).start()
'''
#######################################################################################################################################################
# python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

#n, m = map(int, input().split())
#clauses = [ list(map(int, input().split())) for i in range(m) ]
# may need to add CNFs here
# print(n,m,clauses)

class Vertex:
    def __init__(self,u):
        self.index = u
        self.value = -1 # the value the vertex becomes in the CNF when satisfied
        self.out_neighbors = [] # vertices that can be traversed in the forward direction (u -> v)
        self.in_neighbors = [] # vertices that can be traversed in the backward direction (t -> u)
        self.scc = set() # will hold the set of the strongly connected components this vertex is part of
        self.root = False # will determine if this is the root of the SCC
        # tarjan-specific variables
        self.lowlink = -1 # smallest discovered vertex reachable from this one
        self.discovered = -1 # when it was discovered
        self.on_stack = False

def isSatisfiable(clauses,n,m):
    graph = construct_implication_graph(clauses,n,m)
    # print(graph)
    # print([(v.index, v.out_neighbors, v.in_neighbors) for v in graph.values()])
    roots = find_SCCs(graph, tarjans)
    # roots = find_SCCs(graph, kosaraju)[::-1]
    # print(roots, {root: graph[root].scc for root in roots})
    for vertex in roots:
        if -vertex in graph[vertex].scc:
            return None
        # also check that components and their inverses aren't in the scc
        for literal in graph[vertex].scc:
            if -literal in graph[vertex].scc:
                return None
    # as roots contains the reverse topological order of the sccs, just go backwards and fill solns
    result = [None] * n
    for scc_root in roots:
        # print(graph[scc_root].scc)
        for literal in graph[scc_root].scc:
            if graph[literal].value == -1:
                graph[literal].value = 1
                # print(literal)
                result[abs(literal) - 1] = literal
                # print(result)
                graph[-literal].value = 0
#    print(result)
    return result

def construct_implication_graph(clauses,n,m):
    """
    constructs implication graph in the form of u -> v for clauses.
    returns a dict of vertices in the form {index : Vertex(index)}
    see Vertex object for further info
    """
    graph = {} # u -> v stored as [u,v]
    for i in range(1,n+1):
        # graph[i] = []
        # graph[-i] = []
        graph[i] = Vertex(i)
        graph[-i] = Vertex(-i)
    for clause in clauses:
        u = clause[0]
        if len(clause) == 1:
            # graph.append([-clause[0], clause[0]])
            graph[-u].out_neighbors.append(u)
            graph[u].in_neighbors.append(-u)
            # graph[-u].append(u)
        elif len(clause) == 2:
            v = clause[1]
            # print(u,v)
            # graph.append([-clause[0], clause[1]])
            # graph.append([-clause[1], clause[0]])
            graph[-u].out_neighbors.append(v)
            graph[v].in_neighbors.append(-u)
            graph[-v].out_neighbors.append(u)
            graph[u].in_neighbors.append(-v)
    return graph

def find_SCCs(graph, function):
    """ uses either Kosaraju's or Tarjan's to find SCCs. """
    return function(graph)

def kosaraju(graph):
    """ uses Kosaraju's Algorithm to generate the SCCs. returns a list of vertex roots of the SCCs. potentially bugged as it didn't pass. """
    L = [] #list that stores traversals
    explored = set()
    # visit each vertex via dfs
    for vertex in graph.keys():
        visit(vertex, graph, explored, L)
    # print(L)
    # now assign values to root, forming SCCs
    assigned = set()
    roots = [] # stores roots of SCCs in topological order
    for vertex in L:
        assign(vertex, vertex, graph, assigned, roots)

    # scc_roots_graph = { vertex : graph[vertex] for vertex in graph.keys() if graph[vertex].root }
    # print({vertex : graph[vertex].scc for vertex in scc_roots_graph.keys()}, {vertex : graph[vertex].out_neighbors for vertex in graph.keys()})
    # print(roots)
    return roots

def tarjans(graph):
    """ uses Tarjan's Algorithm to generate the SCCs. returns a list of roots in reverse topological order. """
    index = 0
    stack = []
    roots = []
    for vertex in graph.keys():
        if graph[vertex].discovered == -1:
            strongconnect(graph[vertex], stack, index, graph, roots)
            # print(stack, roots)
    return roots

def strongconnect(vertex, stack, index, graph, roots):
    """ Helper for Tarjan's. Generates the SCCs. vertex input is the Vertex object. """
    vertex.discovered = index
    vertex.lowlink = index
    index += 1
    stack.append(vertex)
    vertex.on_stack = True

    # dfs
    for out_vertex_index in vertex.out_neighbors:
        if graph[out_vertex_index].discovered == -1:
            # not visited; recurse
            strongconnect(graph[out_vertex_index], stack, index, graph, roots)
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].lowlink)
        elif graph[out_vertex_index].on_stack:
            # the vertex is on the stack; back edge case
            # the out_vertex is the root
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].discovered)

    # generate the SCC if conditions are correct
    if vertex.discovered == vertex.lowlink:
        # print(vertex.index)
        # print(vertex.index, [v.index for v in stack])
        # popped_vertex = False
        while len(stack) != 0:
            v = stack.pop(-1)
            vertex.scc.add(v.index)
            v.on_stack = False
            # pop the stack only up and including the current root
            if v == vertex:
                break
        # while vertex != v
        roots.append(vertex.index)

def visit(u, graph, explored, L):
    """
    visits all vertices via dfs
    prepends them to a list L (to keep v from appearing from u) for further processing
    """
    # print(explored, u, u not in explored)
    # print()
    if u not in explored:
        explored.add(u)
        L.insert(0, u)
        for v in graph[u].out_neighbors:
            # print(v, v not in explored, explored)
            visit(v, graph, explored, L)

def assign(u, root, graph, assigned, roots):
    """ assigns all vertices to a SCC via dfs """
    if u not in assigned:
        graph[root].scc.add(u)
        assigned.add(u)
        if u == root:
            graph[u].root = True
            roots.append(u)
        for v in graph[u].in_neighbors:
            assign(v, root, graph, assigned, roots)

#def main():
#if __name__ == "__main__":
#    n, m = map(int, input().split())
#    clauses = [ list(map(int, input().split())) for i in range(m) ]
#    result = isSatisfiable(clauses,n,m)
#    if result is None:
#        print("UNSATISFIABLE")
#    else:
#        print("SATISFIABLE");
##        print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
#        print(" ".join([str(i) for i in result]))

#threading.Thread(target=main).start()
#######################################################################################################################################################  
    

def Stress_testing():
    
#    for i in range(50):
    while(1):
        
#        print("-----------------------------------------------------------")
#        clauses_range = 5
#        variables_start = int(clauses_range/2) # variables should be atleast more than half of no of clauses
#        n = random.randrange(variables_start, clauses_range, 1) # variables range till y in range(x,y,z) 
#        m = random.randrange(1, clauses_range, 1)
#        print(n, m)
#        
#        clauses = []
#        
#        for clause in range(m):
#            
#            clause_length = random.randrange(1, 3, 1) # clause length 1 or 2 # 2
#            single_clause = []
#            randomlist = random.sample(range(-n, n), 2*n) # last argument must be smaller or equal to no's in range(-var, var)
#            if 0 in randomlist:
#                randomlist.remove(0) # because 0 cannot be a literal
#            for literal in range(clause_length):  
#                single_clause.append(random.choice(randomlist)) # choice selects random from list
#            clauses.append(single_clause)
#        print(f"clauses={clauses}") 
        
        
        print("-----------------------------------------------------------")
        n = random.randrange(2,6)
        m = random.randrange(2,6)
        print(n, m)
        
        random_list = list(range(-n, 0)) + list(range(1, n+1))
        clauses = []
        
        for clause_no in range(m):
            
            clause_length = random.randrange(1,3)
            single_clause = set()
            
            while len(single_clause) != clause_length:
                random_number = random.choice(random_list)
#                random_list.remove(random_number)
                single_clause.add(random_number)
                
            clauses.append(list(single_clause))
        
        print(f"clauses={clauses}") 

#        is_satis = isSatisfiable(n, clauses)
#        if is_satis is None:
#            result_1 = "UNSATISFIABLE"
#        else:
#            result_1 = "SATISFIABLE"
       
        is_satis_CC = SAT_2_CNF(n, clauses)
        if is_satis_CC is None:
            result_2 = "UNSATISFIABLE"
        else:
            result_2 = "SATISFIABLE"
            
        pycosat_result = isSatisfiable(clauses,n,m)   
        if pycosat_result is None:
            result_gold = "UNSATISFIABLE"
        else:
            result_gold = "SATISFIABLE"
            
        if (result_gold != result_2):
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(n, m)
            print(f"clauses={clauses}")  
            print(f"result_gold = {result_gold}")
            print(f"result_2 = {result_2}")
            print("Wrong Answer")
            print(f"satisfying_Assignment_SAT_2_CNF = {is_satis_CC}")
            print(f"satisfying_Assignment_isSatisfiable = {pycosat_result}")
            break
        else:
            print(f"result_gold = {result_gold}")
            print(f"result_2 = {result_2}")
            print("Results_Match")
            print(f"satisfying_Assignment_SAT_2_CNF = {is_satis_CC}")
            print(f"satisfying_Assignment_isSatisfiable = {pycosat_result}")
            
if __name__ == "__main__":   
    
    Stress_testing()
       
    
