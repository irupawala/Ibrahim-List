# python3

import math
#import copy
from itertools import permutations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def optimal_path_brute_force(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


def printPowerSet(set):
    
    set_size = len(set)
    pow_set_size = (int) (math.pow(2, set_size)) # set_size of power set of a set with set_size n is (2**n -1)
    power_set = []
    
    for counter in range(pow_set_size):
        sub_set = []
        for binary in range(set_size):
            if ((1 << binary) & counter) > 0:
                sub_set.append(set[binary])
        if 0 in sub_set: # Only adding the subsets with starting point 0 in it
            power_set.append(sub_set)    
    return power_set

def min_dist_last_to_start_node(C, graph):
    n = len(graph)
    min_dist = INF
    for key, value in C.items():
        if len(value['path']) == n: # Only considering the paths which has travelled all the nodes
            if (value['dist'] + graph[key[1]][0]) < min_dist: # key[1] is the node visited last in the path in the dictionary def
                min_dist = value['dist'] + graph[key[1]][0]
                min_path = value['path']
    
    if min_dist < INF:
        return min_dist, min_path       
    else:
        return -1, None
            
def optimal_path_dynamic(graph):
    
    start_node = 0
    
    # Creating list of subsets consisting of start_node
    n = len(graph)
    set = range(n)
    set_with_0 = printPowerSet(set)
    min_return_dist = INF
    
    # Creating distance list of all subsets containing start_node 
    # Distance of subset to each node is assigned INF in the beginning. 
    # This means min dist from 0 to each other node such that all other nodes of the subset is visited exactly once is INF
    # Also to get the path of min distance creating path key and assigning start_node as the first node visited
    C = {}  
#    for x in set_with_0:
#        for last_node in range(n):
#            C[str(x),last_node] = {'dist' : INF, 'path' : [0]}            
#            
    # Dynamic Programming
#    C[str([start_node]),start_node]['dist'] = 0
    C[str([start_node]),start_node] = {'dist' : 0, 'path' : [0]} 
    for size in range(2,n+1): # Considering size of the subsets from 2 to n
        for S in set_with_0: # Considering the subsets of size 2
            if len(S) == size:
#                C[str(S),start_node]['dist']  = INF
                C[str(S),start_node] = {'dist' : INF, 'path' : [0]} 
                for i in S:
                    if i != start_node:
                        for j in S:
                            if j != i:
#                                S_minus_i = copy.deepcopy(S) # Its important to create deep copy because as we change S_minus_i, S also gets changed
                                S_minus_i = S[:] # copy.deepcopy is extremely slow use this method instead
                                S_minus_i.remove(i)     
                                if (str(S),i) not in C.keys(): # Instead of a dictionary having all dist assigned INF only create it for the paths needed
                                    C[str(S),i] = {'dist' : INF, 'path' : [0]}    
                                    
                                min_dist = min(C[str(S),i]['dist'] , C[str(S_minus_i),j]['dist'] + graph[j][i])
                                if C[str(S),i]['dist'] > min_dist:
                                    C[str(S),i]['dist'] = min_dist
#                                    S_path = copy.deepcopy(C[str(S_minus_i),j]['path'])
                                    S_path = C[str(S_minus_i),j]['path'][:]
                                    S_path.append(i)
                                    C[str(S),i]['path'] = S_path  
                                    
                                    # Instead of calling min_dist_last_to_start_node adn runnng separate loop we can find min distance in this loop itself
                                    # It turns out that this way is slow hence using function min_dist_last_to_start_node. Also func makes it more readable
                                    if len(C[str(S),i]['path']) == n:
                                        if (C[str(S),i]['dist'] + graph[i][0]) < min_return_dist:
                                                min_return_dist = C[str(S),i]['dist'] + graph[i][0]
                                                min_path = C[str(S),i]['path']
#   For checking the dictionary C                                                 
#    for key, value in C.items():
#        print(key, value)

# Call this while using loop in this func itself to find min_path                                        
    if min_return_dist < INF:
        return min_return_dist, min_path       
    else:
        return -1, None    
# Call this while using the func to return min_path           
#    return min_dist_last_to_start_node(C, graph)
    
#################################################################   Unit Testing ###############################################################
        
import os

def test():
    
    filename_list = []
    for root, dirs, files in os.walk("./tests"):
        for filename in files:
            if not filename.endswith('.a'):
                filename_list.append(filename)
        filename_list.sort()
        
    for filename in filename_list:
        
        print('---------------------------------------------')
        print('Running Test: ' + filename)
        
        file = "./tests/" + filename
        edge_list = []
        with open(file) as inputs:
            for index, line in enumerate(inputs):
                if index == 0:
                    n, m = map(int, line.split())
                    graph = [[INF] * n for _ in range(n)]
                else:                   
                    u, v, weight = map(int, line.split())
                    edge_list.append([u, v, weight])
                    u -= 1
                    v -= 1
                    graph[u][v] = graph[v][u] = weight
                    
        print(n, m)
        for edge in edge_list:
            print(" ".join(map(str, edge)))
            
        print('------------- Response ------------')
        min_dist, path = optimal_path_dynamic(graph)  
        
        if min_dist == -1:
            print(min_dist)
        else:
            print(min_dist)
            print(" ".join(map(lambda x:str(x+1), path)))
            
        output_file = "./tests/" + filename[:-3] + "a"
        with open(output_file) as outputs:
            expected_min_path = ""
            for index, line in enumerate(outputs):
                if index == 0:
                    expected_min_dist = line.split()
                    expected_min_dist = " ".join(map(str, expected_min_dist))
                    expected_min_dist = int(expected_min_dist)
                else:
                    expected_min_path = list(map(int, line.split()))
                    
            if (expected_min_dist == min_dist):
                print("YYYYYY---Test Passed---YYYYYY")
                print("Expected Response")
                print(expected_min_dist)
                print(" ".join(map(lambda x:str(x), expected_min_path)))
            else:
                print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN---Test Failed---NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
                print("Expected Response")
                print(expected_min_dist)
                print(" ".join(map(lambda x:str(x), expected_min_path)))                
                    
####################################################################################################################################################       

def conv(x):
    return str(x+1)

if __name__ == '__main__':
#    print_answer(*optimal_path_brute_force(read_data()))

    min_dist, path = optimal_path_dynamic(read_data())    
    if min_dist == -1:
        print(min_dist)
    else:
        print(min_dist)
        print(" ".join(map(lambda x:str(x+1), path)))
#        print(" ".join(map(conv, path)))
    
#    test()
        
        
#####################################################################################################################################################
        
'''
Time Complexity: O(n^2. 2^n)
'''
    