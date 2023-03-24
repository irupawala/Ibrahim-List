#Uses python3

#import sys

'''
Runtime is O(|V| + |E|)
'''


def acyclic(adj):
    
    def build_ancestor(index, adj, ancestor, visited):
        visited[index] = True
        for n in adj[index]: # Check the immediate neighbors if they are present in the Ancestors
            if n in ancestor:
                return True
        for n in adj[index]: # If not present in ancestors then loop into the neighbors
            if visited[n] != True:
                if index not in ancestor:
                    ancestor.append(index) #append the index as an ancestor before jumping to immediate neighbor
                if build_ancestor(n, adj, ancestor, visited) == True:
                    return True
        if index in ancestor: # This step is very crucial. don't forget to remove the index from the ancestors list while backtracking because the other path need not have the ancestors found down the line on one path from one node.
            ancestor.remove(index)
        return False
        
    

    visited = [False] * len(adj)
    for index, vertex in enumerate(adj):
        if visited[index] == False:
            ancestor = [] # build a list of visited nodes. If we encounter visited node again then it is a cycle
            if build_ancestor(index, adj, ancestor, visited) == True:
                return True
    return False

if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    
    data = list(map(int, input().split()))    
    
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1) # notice here we don't have adj[b-1]. append[a-1] because here we can't move in both directions like indirectional graph
    print(1 if acyclic(adj) else 0)


##########################################################################################################################
'''
Sample Inputs

4 4 1 2 4 1 2 3 3 1 
5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5 
3 3 1 3 1 2 2 3
3 3 1 2 1 3 2 3 

'''