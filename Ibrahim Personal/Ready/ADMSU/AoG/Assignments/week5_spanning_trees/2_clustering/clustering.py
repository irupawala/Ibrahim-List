#Uses python3
#import sys

'''
To solve this problem apply Kruskal's Algo and keep on adding min length edges till k clusters (sets)
are created. After k sets has been made the min distance calculated between any two sets is the 
the largest possible value of 𝑑 such that the given points can be partitioned into 𝑘 non-empty subsets
in such a way that the distance between any two points from different subsets is at least 𝑑.

Running Time - T(CalculateWeight) + T(MakeSet) + |E|(T(Find)) + |V|T(Union) =~ O(|V|^2) + O(|V|) + O((|E|+|V|)log|V|) with Disjoint sets
Running Time - T(CalculateWeight) + T(MakeSet) + |E|(T(Find)) + |V|T(Union) =~ O(|V|^2) + O(|V|) + O((|E|+|V|)(1)) with Dict Disjoint sets 
 
'''
import math

def CalculateWeight(x, y):
    
    vertices = list(zip(x, y))
    weight_vertex = {}
    for index, vertex in enumerate(vertices):
        for i, v in enumerate(vertices):
            if i != index:
                key = str(index) + "-" + str(i)
                reverse_key = str(i) + "-" + str(index)
                if(key not in weight_vertex.keys() and reverse_key not in weight_vertex.keys()):
                    weight_vertex.update({key : math.sqrt( (vertices[index][0]-vertices[i][0])**2 + (vertices[index][1]-vertices[i][1])**2 ) })
    return weight_vertex


def FindMinDistElement(weight):
    values_list = list(weight.values())
    keys_list = list(weight.keys())
    min_distance_element = min(values_list) 
    min_index = keys_list[values_list.index(min_distance_element)] #Extracting the index of min distance
    del(weight[min_index]) # deleting min distance
    return weight, min_distance_element, min_index

def FindMinDist(weight):
    values_list = list(weight.values())
    min_distance_element = min(values_list) 
    return min_distance_element

def MakeSet(x):
    sets = {x:{x} for x in range(x)}
    return sets

def Find(Sets, x):
    keys_list = list(Sets.keys())
    values_list = list(Sets.values())
    
    for index, vertex in enumerate(values_list):
        if x in vertex:
            required_set_no = keys_list[values_list.index(vertex)]
            return required_set_no            

def Union(Sets, set_u, set_v):
    element_union = Sets[set_u].union(Sets[set_v])    
    Sets[set_u] = element_union
    del(Sets[set_v]) 
    return Sets


def clustering(x, y, k):
    #write your code here
    weight = CalculateWeight(x, y) #Notice here that as the neighbors are not given we will consider all nodes as neighbors
    Sets = MakeSet(len(x))
    MST_Set = set()
    

    code_iterations = (len(weight)) + 1 

    for vertex in range(code_iterations):
        weight, min_dist, min_dist_key = FindMinDistElement(weight)
        vertices = min_dist_key.split("-")
        u = int(vertices[0])
        v = int(vertices[1])
        key_u = Find(Sets, u)
        key_v = Find(Sets, v)
        
        if key_u != key_v :         
            if len(Sets) == k: # Make sets equal to k
                largest_dist_bet_k_clusters = min_dist # the min_dist obtained after k sets are created is max 
                return largest_dist_bet_k_clusters # between the clusters as we are sorting w.r.t. min edge weight      
            MST_Set.add(u)
            MST_Set.add(v)            
            Sets = Union(Sets, key_u, key_v)


if __name__ == '__main__':
    
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    data = list(map(int, input().split()))    
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
    
    

'''
12 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3
6 5 1 4 4 7 6 7 8 2 7 2 8 3
8 5 1 4 4 4 3 1 7 2 7 2 8 7 6 7 8 3
8 7 6 7 8 6 7 4 4 3 3 1 7 2 7 2 8 3 
8 3 1 1 2 4 6 9 8 9 9 8 9 3 11 4 12 4
7 3 1 1 2 4 6 8 9 9 9 8 9 4 12 4
6 3 1 1 2 4 6 8 9 9 9 4 12 4
7 3 1 1 2 4 6 8 9 9 9 4 11 4 12 4
4 0 0 0 1 1 0 1 1 2
2 0 0 0 1 2
'''