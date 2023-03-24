# python3


import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self,u):
        self.index = u
        self.value = -1 # the value the vertex becomes in the CNF when satisfied
        self.neighbors = [] # vertices that can be traversed in the forward direction (u -> v)

        self.scc = set() # will hold the set of the strongly connected components this vertex is part of
        # self.root = False # will determine if this is the root of the SCC
        
        # tarjan-specific variables
        self.lowlink = -1 # smallest discovered vertex reachable from this one
        self.discovered = -1 # when it was discovered
        self.on_stack = False

def isSatisfiable(clauses,n,m):
    graph = construct_implication_graph(clauses,n,m)
    
    # find SCC's after creating implication graph
    roots = find_SCCs(graph, tarjans)

    # check that roots and their inverses aren't in the scc
    for vertex in roots:
        if -vertex in graph[vertex].scc:
            return None
        # also check that SCC's other nodes and their inverses aren't in the scc
        for literal in graph[vertex].scc:
            if -literal in graph[vertex].scc:
                return None
            
    # as roots contains the reverse topological order of the sccs, just go backwards and fill solns
    result = [None] * n
    for scc_root in roots:
        for literal in graph[scc_root].scc:
            if graph[literal].value == -1:
                graph[literal].value = 1                
                graph[-literal].value = 0
                
                result[abs(literal) - 1] = literal

    return result

def construct_implication_graph(clauses,n,m):
    """
    constructs implication graph in the form of u -> v for clauses.
    returns a dict of vertices in the form {index : Vertex(index)}
    see Vertex class for further info
    """
    graph = {} # u -> v stored as [u,v]
    
    for i in range(1,n+1):
        graph[i] = Vertex(i)
        graph[-i] = Vertex(-i)
        
    for clause in clauses:
        u = clause[0]
        if len(clause) == 1:
            graph[-u].neighbors.append(u)

        elif len(clause) == 2:
            v = clause[1]
            graph[-u].neighbors.append(v)
            graph[-v].neighbors.append(u)

    return graph

def find_SCCs(graph, function):
    """ uses either Kosaraju's or Tarjan's to find SCCs. """
    return function(graph)

def tarjans(graph):
    """ uses Tarjan's Algorithm to generate the SCCs. returns a list of roots in reverse topological order. """
    index = 0 # to give each node a unique index
    stack = []
    roots = [] # stores the starting node of each SCC
    for vertex in graph.keys():
        if graph[vertex].discovered == -1:
            strongconnect(graph[vertex], stack, index, graph, roots)
    return roots

def strongconnect(vertex, stack, index, graph, roots):
    """ Helper for Tarjan's. Generates the SCCs. vertex input is the Vertex object. """
    vertex.discovered = index # Mark the vertex discovered
    vertex.lowlink = index # Give the lowlink value of vertex as index currently
    index += 1
    stack.append(vertex) # Keep on appending the vertex untill no new vertex can be explored in this chain
    vertex.on_stack = True

    # dfs
    for out_vertex_index in vertex.neighbors:
        if graph[out_vertex_index].discovered == -1:
            # not visited; recurse
            strongconnect(graph[out_vertex_index], stack, index, graph, roots)
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].lowlink)
        elif graph[out_vertex_index].on_stack:
            # the vertex is on the stack; back edge case
            # the out_vertex is the root
            vertex.lowlink = min(vertex.lowlink, graph[out_vertex_index].lowlink)

    # generate the SCC if conditions are correct
    if vertex.discovered == vertex.lowlink: # start popping the stack when dfs has returned back to the root

        while len(stack) != 0:
            v = stack.pop(-1)
            vertex.scc.add(v.index)
            v.on_stack = False
            # pop the stack only up and including the current root
            if v == vertex: # If root is reached, stop
                break

        roots.append(vertex.index) #append the root in the list once all the nodes in the same SCC has been removed from stack

def main():
#if __name__ == "__main__":
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
 
    result = isSatisfiable(clauses,n,m)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");

        print(" ".join([str(i) for i in result]))

threading.Thread(target=main).start()

"""

Implement the algo described in the slides.
Use tarjan's algo discussed https://www.youtube.com/watch?v=TyWtx7q2D7Y to find SCC's
Notice that it is crucial to assign literals in reverse topological order that is the main reason of using Tarjan's algo over Kosaraju

Running time is O(|F|) (linear time in function of Formula F)
Each step creating implication graph, finding SCC's, assigning value to literal is linear in time
 
"""