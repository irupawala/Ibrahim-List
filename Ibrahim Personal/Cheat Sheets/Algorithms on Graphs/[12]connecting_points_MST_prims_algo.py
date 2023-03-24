#Uses python3
#import sys
import math

'''
Note that the Algorithm is exactly same as Djikstra's Algo, The only difference being instead of comparing total distance from the root node, min cost of 
each node w.r.t any other node is calculated.

Running time is O(|E|log|V|)
'''


def CalculateWeight(x, y):
    
    vertices = list(zip(x, y))
    weight_vertex = [False] * len(vertices) # calculating weight from each vertex to every other vertex
    
    for index, vertex in enumerate(vertices):
        weight_vertex[index] = [math.sqrt((vertices[index][0]-a)**2 + (vertices[index][1]-b)**2) for (a, b) in vertices]
    
#    weight = {index: weight_single_vertex for index, weight_single_vertex in enumerate(weight_single_vertex)} # creating a dictionary for each vertex with it's distance to every other inclusing its own    
    return weight_vertex
    
def MakeQueue(cost):
    H = {index: cost for index, cost in enumerate(cost)} #using dictionary as it does not change the index upon deletion of an element
    return H
    
def ExtractMin(H):
    values_list = list(H.values())
    keys_list = list(H.keys())
    min_distance_element = min(values_list) 
    min_index = keys_list[values_list.index(min_distance_element)] #Extracting the index of min distance
    del(H[min_index]) # deleting min distance
    return (min_index)
   
def ChangePriority(PrioQ, v, dist):
    PrioQ[v] = dist # updating the distance values in H
    return 0
    
def CalculateDistance(cost):
    distance = sum(cost)
        
    return distance
    
    
def minimum_distance(x, y):
    result = 0.
    
    weight = CalculateWeight(x, y) #Notice here that as the neighbors are not given we will consider all nodes as neighbors
    cost = [100000] * len(x) # cost is dist in dijkstra
    cost[0] = 0
    
    PrioQ = MakeQueue(cost) # Index and Distance as keys
    
    while len(PrioQ) != 0:
        v = ExtractMin(PrioQ)

        for index, vertex in enumerate(weight[v]):
            if index != v: 
                if (index in list(PrioQ.keys()) and cost[index] > vertex): # Here notice that it is very important to check if index in list(PrioQ.keys()), 
                                                                           # because we want to calculate minimum distance for only those elements for which min distance is not yet calculated
                    cost[index] = vertex
                    ChangePriority(PrioQ, index, cost[index])   
                    
    result = CalculateDistance(cost)                 
    return result


if __name__ == '__main__':
    
#    input = sys.stdin.read()    
#    data = list(map(int, input.split()))
    
    
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    
     
    
    print("{0:.9f}".format(minimum_distance(x, y)))
    

'''

4 0 0 0 1 1 0 1 1 
4 1 2 3 4 5 6 7 8 
5 0 0 0 2 1 1 3 0 3 2 
4 0 0 1 1 2 2 3 3 4 4 
13 1 58 28 80 42 84 89 54 44 28 36 64 54 39 20 14 66 41 36 84 24 84 16 64 9 80

'''