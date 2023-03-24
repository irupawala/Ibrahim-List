INF = 10 ** 9
#def read_data():
#    n, m = map(int, input().split())
#    graph = [[INF] * n for _ in range(n)]
#    for _ in range(m):
#        u, v, weight = map(int, input().split())
#        u -= 1
#        v -= 1
#        graph[u][v] = graph[v][u] = weight
#    return graph

def printPowerSet(set):
    
    set_size = len(set)
    pow_set_size = (int) (2**set_size)
    power_set = []
    
    for counter in range(pow_set_size):
        sub_set = []
        for binary in range(set_size):
            if ((1 << binary) & counter) > 0:
                sub_set.append(set[binary])
        if 0 in sub_set: # Only adding the subsets with starting point 0 in it
            power_set.append(sub_set)    
    return power_set

def optimal_path_dynamic(graph):
    
    start_node = 0
    n = len(graph)
    set = range(n)
    set_with_0 = printPowerSet(set)
    min_return_dist = INF
    C = {}  

    C[str([start_node]),start_node] = {'dist' : 0, 'path' : [0]} 
    for size in range(2,n+1): # Considering size of the subsets from 2 to n
        for S in set_with_0: # Considering the subsets of size 2
            if len(S) == size:

                C[str(S),start_node] = {'dist' : INF, 'path' : [0]} 
                for i in S:
                    if i != start_node:
                        for j in S:
                            if j != i:
                                S_minus_i = S[:] # copy.deepcopy is extremely slow use this method instead
                                S_minus_i.remove(i)     
                                if (str(S),i) not in C.keys(): # Instead of a dictionary having all dist assigned INF only create it for the paths needed
                                    C[str(S),i] = {'dist' : INF, 'path' : [0]}    
                                    
                                min_dist = min(C[str(S),i]['dist'] , C[str(S_minus_i),j]['dist'] + graph[j][i])
                                if C[str(S),i]['dist'] > min_dist:
                                    C[str(S),i]['dist'] = min_dist
                                    S_path = C[str(S_minus_i),j]['path'][:]
                                    S_path.append(i)
                                    C[str(S),i]['path'] = S_path  

                                    if len(C[str(S),i]['path']) == n:
                                        if (C[str(S),i]['dist'] + graph[i][0]) < min_return_dist:
                                                min_return_dist = C[str(S),i]['dist'] + graph[i][0]
                                                min_path = C[str(S),i]['path']
                                  
    if min_return_dist < INF:
        return min_return_dist, min_path       
    else:
        return -1, None    
    
if __name__ == '__main__':

    # graph generated to reduce steps in pythontutor for example 1 in the assignment
    min_dist, path = optimal_path_dynamic([[1000000000, 20, 42, 35], [20, 1000000000, 30, 34], [42, 30, 1000000000, 12], [35, 34, 12, 1000000000]])    
#    min_dist, path = optimal_path_dynamic(read_data())    
    if min_dist == -1:
        print(min_dist)
    else:
        print(min_dist)
        print(" ".join(map(lambda x:str(x+1), path)))
