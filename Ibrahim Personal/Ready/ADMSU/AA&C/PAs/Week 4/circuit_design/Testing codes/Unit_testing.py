# python3

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

#######################################################################################################################################################
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

    for scc in scc_list:
        for literal in scc:
            
            index = abs(literal)
            if literals[index] == None:
                literals[literal] = 0
                literals[-literal] = 1

    return(list(literals.values()))
    
########################################################################################################################################################
    
def Satifiability_FAST(n, clauses):
    
    result = SAT_2_CNF(n, clauses)
    
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        result_list = [-i-1 if result[i] else i+1 for i in range(n)]
        print(" ".join(map(str, result_list)))    

############################################# Unit Testing ###############################################
    
import os     
def test():
    

    filename_list = []
    for root, dirs, files in os.walk("./large_tests"):
        for filename in files:
#            if '.a' not in filename:
            if not filename.endswith('.a'): 
                filename_list.append(filename)
                filename_list.sort()
                
    for filename in filename_list:
        
        print('........................')
        print('Running Test: ' + filename)
        
        file = "./large_tests/" + filename
        with open(file) as inputs:
            for index, line in enumerate(inputs):
                if index == 0:
                    n, m = map(int, line.split())   
                else:
                    clauses = [ list(map(int, line.split())) for i in range(m) ]
                    

            
#        f=open("./tests/" + filename, "r")
#        if f.mode == 'r':
##            test_input = f.read().rstrip('\n')
#            n =  f.readline()
#            f.close()
#               
#        print(n, m)
#        print(clauses)
        
        Satifiability_FAST(n, clauses)
#        print(type(test_input))
#        f=open("./tests/" + filename + '.a', "r")
#        if f.mode == 'r':
#            expected_output =f.read().rstrip('\n')
#            f.close()
#            
#        output = Satifiability_FAST(n, clauses)
#        
# 
#        print('Input: ' + str(test_input))
#        print('Expected Output: ' + str(expected_output))
#        print('Ouput: ' + str(output))
#
#
#
#        if str(expected_output)==str(output):
#            print('Test Passed')
#        else:
#            print('Test Failed')
#            break    
#
#    print("Passed all tests !!")
#       

#############################################################################################################


if __name__ == "__main__":
#def main():    
#    n, m = map(int, input().split())
#    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
#    Satifiability_FAST(n, clauses)
    test()
    


