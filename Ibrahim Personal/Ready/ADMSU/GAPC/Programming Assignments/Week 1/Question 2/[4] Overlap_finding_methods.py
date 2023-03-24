# python3

'''

Tried all this methods to find a way to compute overlap fast however with all these methods too
code does not pass the "TIME EXCEEDED LIMIT" ERROR


'''

import datetime
start_time = datetime.datetime.now()

# Naive Algorithm to find overlap between node and neighbor using For loop
def find_overlap_naive_for(node, neighbor):
    min_overlap_len = 16
    overlap_string = neighbor[0:min_overlap_len]
    error_limit = 2
    
    for start in range(len(node)-min_overlap_len): 
        error_counter = 0
        start_counter = start
  
        for overlap_index in range(min_overlap_len): # For each character in node checking if min_overlap exists
            if error_counter > error_limit:
                break
            if node[start_counter] is not overlap_string[overlap_index]:
                error_counter += 1
            start_counter += 1
            continue
        
        if error_counter <= error_limit: # Chcking if remaining of the node is extended to neighbor
            remaining_node_len = len(node)-start_counter
            for y in range(remaining_node_len): # Checking if remaining of the node is similar to the neighbor
                if error_counter > error_limit:
                    break
                neighbor_index = min_overlap_len + y
    
                if node[start_counter] is not neighbor[neighbor_index]:
                    error_counter += 1 
                start_counter += 1
                continue             
        
        # If error>2 after the matching go to next char of node         
        if error_counter > error_limit:
            continue
    
        overlap_start = start
        overlap_length = len(node) - overlap_start
        return (overlap_start, overlap_length)
    
    return (-1, 0) # return (-1, 0) if no match found
    
# Trying Regex Algo to find max overlap
def find_overlap_regex(node, neighbor):
    import regex
    min_overlap_len = 16
    overlap_string = neighbor[0:min_overlap_len]
    matches_index = []
    for match in regex.finditer(r"(" + overlap_string+ "){s<=0}", node):
        s = match.start()
        matches_index.append(s)
    if len(matches_index) == 0:
        return (-1, 0)
    overlap_start = max(matches_index)
    overlap_length = len(node) - overlap_start  
    return (overlap_start, overlap_length)

# find function for finding overlap for error free reads
def find_overlap_find(node, neighbor):
    min_overlap_len = 4
    
    start = 0
    while True:
        start = node.find(neighbor[0:min_overlap_len], start)
        if start == -1:
            return (-1, 0)
        if neighbor.startswith(node[start:]):
            overlap_start = start
            overlap_length = len(node) - overlap_start
            return (overlap_start, overlap_length)
        start += 1

# Naive Algorithm to find overlap between node and neighbor using While loop
def find_overlap_naive_while(node, neighbor):
    min_overlap_len = 4
    overlap_string = neighbor[0:min_overlap_len]
    error_limit = 0
    start = 0 
    
    while start < len(node) - min_overlap_len:
        error_counter = 0
        start_counter = start        
        
        overlap_index = 0
        while overlap_index < min_overlap_len:
            if error_counter > error_limit:
                break
            if node[start_counter] is not overlap_string[overlap_index]:
                error_counter +=1
            overlap_index += 1
            start_counter += 1
            
        if error_counter <= error_limit:
            while start_counter < len(node):
                if error_counter > error_limit:
                    break
                if node[start_counter] is not neighbor[overlap_index]:
                    error_counter +=1
                overlap_index += 1
                start_counter += 1
                
        if error_counter <= error_limit:
            return (start, len(node)-start)
        start += 1
        
    return(-1, 0)
    
# Naive Algorithm to find overlap between node and neighbor using While loop completely scanning the node from the start    
def find_overlap_naive_while_NO_min_Overlap(node, neighbor):
    
    min_overlap_len, error_limit, start, start_counter, error_counter, overlap_index = 4, 0, 0, 0, 0, 0
    
    while start < len(node) - min_overlap_len:       
        if error_counter > error_limit:
            error_counter, overlap_index = 0, 0
            start+=1
            start_counter = start 
            continue
        if node[start_counter] is not neighbor[overlap_index]:
            error_counter += 1
        overlap_index +=1
        start_counter +=1
                
        if error_counter <= error_limit and start_counter == len(node):
            return (start, len(node)-start)
        
    return(-1, 0)    
        
    
print(find_overlap_naive_while_NO_min_Overlap("ATTTATGCGCGCTTCGATAAAAATGATTGGCGTATCCAACCTGCAGAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAG", "AAAATGATTGGCGTATCCAACCTGCAGAGTTTTATCGCTTCCATGACGCAGAAGTTAACACTTTCGGATATTTCTGATGAGTCGAAAAATTATCTTGATA"))  
#print(find_overlap_naive_optimized_1("GATGATGATGCT", "GATGATGCTCTC"))  
#print(find_overlap_naive_optimized_1("GATGATGATGCT", "1561561651")) 

end_time = datetime.datetime.now()
delta = end_time - start_time

print("--- %s microseconds ---" % (delta.microseconds))