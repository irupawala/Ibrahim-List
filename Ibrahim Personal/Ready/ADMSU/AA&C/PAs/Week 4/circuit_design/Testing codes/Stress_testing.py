import random 
import pycosat

def isSatisfiable(n, clauses):
# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.      
    for mask in range(1<<n): # 1 << n is equilvalent to 2 ^ n
        result = [ (mask >> i) & 1 for i in range(n) ] # Generating binary from decimal. Bringing each no to index 0 and ANDING it with 1 to generate bit
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True  
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True 
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

#################################################################################################################################################
def post_order_to_index_convert(post_order):
    
    sorted_by_values_dict = dict(sorted(post_order.items(), key=lambda x: x[1], reverse=True))
    post_order_vertex = list(sorted_by_values_dict.keys())
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

    visited = {n:False for n in adj_list.keys()}
    post_order = {n:-1 for n in adj_list.keys()}
    connected_comp = 0
    clock = 0
    #write your code here
    for key, value in adj_list.items():
        if visited[key] == False:
            clock, post_order = explore_post_order(adj_list, visited, post_order, key, clock)
            connected_comp = connected_comp + 1
        
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
    connected_comp = 0
    clock = 0
    scc_list = []

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
#    return (connected_comp_adj)
    return(scc_list)
#######################################################################################################################################################

def implicationGraph(n, clauses):

    adj = {n:[] for n in range(1,n+1)}
    for n in range(1,n+1):
        adj[-n] = []
        
    adjr = {n:[] for n in range(1,n+1)}
    for n in range(1,n+1):
        adjr[-n] = []
        
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
        
    return adj, adjr


#######################################################################################################################################################
    
def SAT_2_CNF(n, clauses):
    
    adj, adjr = implicationGraph(n, clauses)
    scc_list = number_of_strongly_connected_components(adj, adjr)    
    
    for x in range(1,n+1):
        for scc in scc_list:
            if ((x in scc) and (-x in scc)):
                return None
                
    literals = {n:None for n in  range(1, n+1)}
    
    
#    print(literals)
#    print(scc_list)
    
    for scc in scc_list:
#    for scc in reversed(scc_list):    
        for literal in scc:
            
            index = abs(literal)
            if literals[index] == None:
#                if literal > 0:
                literals[literal] = 0
                literals[-literal] = 1
#                elif literal < 0:
#                    literals[-literal] = 1
#                    literals[literal] = 0
            
#            if literal > 0:
#                 if literals[literal] == None:
#                    literals[literal] = literal      
#                    
#            else:
#                if literals[-(literal)] == None:
#                    literals[-(literal)] = literal
                         
#    print(literals)
    return(list(literals.values()))
#    print(" ".join(map(str,literals.values())))   
    
#######################################################################################################################################################  
    

def Stress_testing():
    
#    for i in range(5):
    while(1):
        
        print("-----------------------------------------------------------")
        clauses_range = 10
        variables_start = int(clauses_range/2) # variables should be atleast more than half of no of clauses
        n = random.randrange(variables_start, clauses_range, 1) # variables range till y in range(x,y,z) 
        m = random.randrange(1, clauses_range, 1)
        print(n, m)
        
        clauses = []
        
        for clause in range(m):
            
            clause_length = random.randrange(1, 3, 1) # clause length 1 or 2 # 2
            single_clause = []
            randomlist = random.sample(range(-n, n), 2*n) # last argument must be smaller or equal to no's in range(-var, var)
            if 0 in randomlist:
                randomlist.remove(0) # because 0 cannot be a literal
            for literal in range(clause_length):  
                single_clause.append(random.choice(randomlist)) # choice selects random from list
            clauses.append(single_clause)
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
            
        pycosat_result = pycosat.solve(clauses)    
        if pycosat_result == "UNSAT":
            result_gold = "UNSATISFIABLE"
        else:
            result_gold = "SATISFIABLE"
            
        if (result_gold != result_2):
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(n, m)
            print(f"clauses={clauses}")  
            break
        else:
            print(f"result_gold = {result_gold}")
            print(f"result_2 = {result_2}")
            print("Results_Match")
            
if __name__ == "__main__":   
    
    Stress_testing()
       
    
