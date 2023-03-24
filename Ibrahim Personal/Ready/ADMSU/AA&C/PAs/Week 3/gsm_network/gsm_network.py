# python3

'''
For this PA, Ignore the outputs given in PDF file for Examples 1 and 2. 

The Problem of Graph Coloring is NP_Complete hence to solve it we need SAT Solver.
To find the satisfying assignment for this scenario we need to fed the following clauses to SAT Solver 

1. Exactly one is True: 
    
for each vertex 𝑖 of the initial graph and each possible color 𝑗 , 1 ≤ 𝑗 ≤ 3 
which means “vertex 𝑖 has color 𝑗 ”. Think how to write down conditions like “each vertex has to be coloredby some color”

This is achieved by the formula (ℓ1 ∨ ℓ2 ∨ ℓ3) (-ℓ1 ∨ -ℓ2) (-ℓ1 ∨ -ℓ3) (-ℓ2 ∨ -ℓ3)

2. Vertices connected by an edge must have different colors 

This is acheived by the formula (-ℓ1 ∨ -ℓ2), meaning both the literals cannot be true together 

'''
import itertools

clauses = []

def exactly_one_of(literals):
    clauses.append([l for l in literals]) #  we first add a clause that contains all the literals in the list literals

#    for pair in itertools.product(literals, repeat=2): # then for all pair of literals we add a clause containing two negated literals from this list    
    for pair in itertools.combinations(literals, 2):  
        clauses.append([-l for l in pair]) 
        
def one_adj_node_false(vertice1, vertice2):

    for no_colors in range(len(vertice1)): # Eg with the current variable naming scheme vertex 1 & 4, 2 & 5 and 3 & 6 should not have same color
        adj_node_false = []
        adj_node_false.append(-vertice1[no_colors])
        adj_node_false.append(-vertice2[no_colors])
        clauses.append(adj_node_false) 

        
def printEquisatisfiableSatFormula(n, m, edges):

# Notice that in this code we are representing vertex 1 having 3 different colors as 1, 2, 3. vertex 2 with 3 different colors as 4, 5, 6 and so on
    
    total_vertices = range(1,n+1)
    
    vertices = [] # contains sublist for each vertex with all three different colors
    current_colored_vertex = 0
    
    for vertex in total_vertices:
        vertex_colors = [] # represents sublist of different colors of the same vertex
        for color in range(3):
            current_colored_vertex += 1
            vertex_colors.append(current_colored_vertex)
        vertices.append(vertex_colors) #Appending sublist containing all different colors of the vertex to the list vertices
    
    # Adding clauses for exactly one of. This signifies that each vertex need to have exactly one color
    for colors in vertices:
        exactly_one_of(colors) 
    
    # Adding clauses for vertices connected by an edge must have different colors      
    for [i,j] in edges:
        one_adj_node_false(vertices[i-1], vertices[j-1])
        
    # Appending clauses with 0 to comply with DIMACS Format
    for c in clauses:
        c.append(0)
    
    print(len(clauses), end=" ")
    print(len(vertices)*3) # because vertices is a list containing sublist of each vertex with 3 different colors
    
    # printing each clause
    for c in clauses:  
        print(" ".join(map(str, c)))    

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m) ]
    
    printEquisatisfiableSatFormula(n, m, edges)