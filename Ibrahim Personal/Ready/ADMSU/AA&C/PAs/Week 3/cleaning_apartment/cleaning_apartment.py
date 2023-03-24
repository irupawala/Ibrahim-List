# python3

'''
########################################################################################
We will be using the naming convention for this Problem as follows :

Different vertices has different positions. Hence let's say if we have 3 vertices then 
1, 2, 3 signifies vertex 1 at position 1,2,3
4, 5, 6 signifies vertex 2 at position 1,2,3
7, 8, 9 signifies vertex 3 at position 1,2,3
########################################################################################

########################################################################################
Consider the example where vertex 1 is connected to 2 and 2 to 3 for sake of simplicity
########################################################################################

For this PA, Ignore the outputs given in PDF file for Examples 1 and 2. 

The Problem of Hamiltonian Path is NP_Complete hence to solve it we need SAT Solver.
To find the satisfying assignment for this scenario we need to fed the following clauses to SAT Solver 

1. Each vertex belongs to a path (function NodeMustAppearInPath()): 

Example vertex 1 has be present in any one of the positions 1, 2, 3 hence (1 V 2 V 3)

2. Each vertex should appear just once in a path (function NoNodeAppearsTwice()):
    
Example vertex 1 can be present in just one position in the path hence (-1 V -2), (-1 V -3), (-2 V-3) are all the unique combinations which has to be added

3. Each position in a path is occupied by some vertex (function EveryPositionMustbeOccupied()):
    
Example from vertex 1 at position 1 (signified as variable 1), vertex 2 at position 1 (signified as variable 4) and vertex 3 at position 1 (signified as variable 7)
any one of them must be present at position 1 of the path hence (1 V 4 V 7) has to be added as a clause

4. No two vertices occupy the same position of a path (function NoTwoNodesInSamePosition()):
    
Example None of the 3 vertices can be at the same position 1 simultaneously hence (-1 V -4), (-1 V -7), (-4 V -7) has to be added    
    
5. Two successive vertices on a path must be connected by an edge (function NonAdjacentVertices()):

In other words, if there is no edge {𝑖, 𝑗} in 𝐸, then for any 𝑘, it cannot be the case that both xik and xj(k+1) are True 
In our example there is no edge between 1 and 3 vertex hence it cannot be the case that 

vertex 1 be at position 1 and 3 be at adjacent position 8 hence (-1 V -8)
vertex 3 be at position 7 and 1 be at adjacent position 2 hence (-7 V -2)
vertex 1 be at position 2 and 3 be at adjacent position 9 hence (-2 V -9)
vertex 3 be at position 8 and 1 be at adjacent position 3 hence (-8 V -3)

'''

import itertools

clauses = []

def NodeMustAppearInPath(literals):
    clauses.append([l for l in literals]) 
    
def NoNodeAppearsTwice(literals):
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def EveryPositionMustbeOccupied(literals):
    clauses.append([l for l in literals]) 
    
def NoTwoNodesInSamePosition(literals):
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])  
        
def NonAdjacentVertices(n, possible_edges, edges):
    
    iterable_positions = range(1, n)
    for (edge_start,edge_end) in possible_edges:
        if (edge_start, edge_end) not in edges and (edge_end, edge_start) not in edges:
            for pos in iterable_positions:
                clauses.append([-(((edge_start-1)*n)+pos), -(((edge_end-1)*n)+pos+1)])
                clauses.append([-(((edge_end-1)*n)+pos), -(((edge_start-1)*n)+pos+1)])            

def printEquisatisfiableSatFormula(n, m, edges):
    
    total_vertices = range(1, n+1)
    total_positions = range(1, n+1)
    
    vertices_list = [] # Contains sublist for each vertex at each position 
    current_position = 0
    
    for vertex in total_vertices:
        vertex_positions = [] # represent a list of vertex at different positions 
        for position in range(n):
            current_position += 1
            vertex_positions.append(current_position)
        vertices_list.append(vertex_positions)
        
    for position in range(len(total_positions)):
        position_n = [vertex[position] for vertex in vertices_list]
        NodeMustAppearInPath(position_n)
        NoNodeAppearsTwice(position_n)                

    for vertex in vertices_list:
        EveryPositionMustbeOccupied(vertex)
        NoTwoNodesInSamePosition(vertex)

    possible_edges = list(itertools.combinations(total_vertices,2))
    NonAdjacentVertices(n, possible_edges, edges)
    
    # Appending clauses with 0 to comply with DIMACS Format    
    for c in clauses:
        c.append(0)
    
    print(len(clauses), end=" ")
    print(n*n)
    
     # printing each clause
    for c in clauses:
        print(" ".join(map(str, c)))

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    edges = [ tuple(map(int, input().split())) for i in range(m) ]
    
    printEquisatisfiableSatFormula(n, m, edges)

