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


cost = [100000] * 5
PrioQ = MakeQueue(cost) # Index and Distance as keys
v = ExtractMin(PrioQ)
index = 1
cost[index] = 10
ChangePriority(PrioQ, index, cost[index])   
