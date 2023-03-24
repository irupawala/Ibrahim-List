# uses python3

import itertools
import sys
import threading
sys.setrecursionlimit(200000)

class Nodes():
    
    def __init__(self, node_string):
        self.node_string = node_string
        self.neighbors = []
        self.in_degree = 0
        self.out_degree = 0

class flowGraph():
    
    def __init__(self):
        self.path_list = {} # Global path dictionary to append all the paths with length greater then threshold, key is startnode_endnode
        self.reads, self.kmer_len, self.bubble_threshold = self.readInputs()
        self.edges_list, self.nodes_list = self.createNodesList()
        self.multiple_indegree, self.multiple_outdegree = self.buildDeBruijnGraph()
        self.findPossibleBubblePath()      
        print(self.findBubbles())
        
#        self.printNodes()
#        self.printPath()        
#        print(f"multiple_indegree = {self.multiple_indegree}")
#        print(f"multiple_outdegree = {self.multiple_outdegree}")

        
    def readInputsTesting(self):
        kmer_len = 4
        bubble_threshold = 4
#        reads = ['AACG', 'AAGG', 'ACGT', 'AGGT', 'CGTT', 'GCAA', 'GGTT', 'GTTG', 'TGCA', 'TTGC'] #3 3 
#        reads = ['ATGCCGTATG', 'GCCGTATGGA', 'GTATGGACAA', 'GTATGGACAA', 'CGTACGGACA', 'CGTATGGACA'] #5 5
        reads = ['AAACGCGTTGAACCCTCAAT', 'GAATTGGAAACACGTTGAAT', 'TGGAAACGCGTTGAACCCTC', 'TGGAAACGCGTTGAACCCTC'] #4 4
#        reads = ['AAABBBA', 'AABCCBA', 'AAABBCBA'] #3 4 
#        reads = ['ATCCTAG', 'TCCTAGA', 'ATCGTCA', 'CGTCAGA', 'CGTTTCA', 'TTTCAGA'] #4 6
#        reads = ['AABBAABB'] #3 1
#        reads = ['AABACBADAA'] #3 6
#        reads = ['AABBA', 'AACBA', 'AADBA'] #3 3
#        reads = ['AACG', 'CGTT', 'TTAA', 'AATG', 'TGTT', 'ACCT', 'CCTT'] # 3 3
        return reads, kmer_len, bubble_threshold
  


    def readInputs(self):      
        input = sys.stdin.read()
        _input = list(map(str, input.split()))
        kmer_len, bubble_threshold = int(_input[0]), int(_input[1])
        reads = _input[2:]
        
        return reads, kmer_len, bubble_threshold
    
    def buildDeBruijnGraph(self):
        multiple_indegree = set()
        multiple_outdegree = set()
        
        for edge in self.edges_list:
            prefix_node = edge[:-1]
            suffix_node = edge[1:] 
            
            prefix_obj = self.nodes_list[prefix_node]
            suffix_obj = self.nodes_list[suffix_node]
            
            if prefix_node != suffix_node: # because self loop of length 1 is not allowed
                if suffix_node not in prefix_obj.neighbors: # because in the de-bruijn graph edges should be added only once
                    prefix_obj.neighbors.append(suffix_node)
                    prefix_obj.out_degree += 1 # creating out-degree for out node
                    suffix_obj.in_degree += 1
                
                if prefix_obj.out_degree > 1: multiple_outdegree.add(prefix_node) # Storing nodes with > 1 in_degree
                if suffix_obj.in_degree > 1: multiple_indegree.add(suffix_node)

        return list(multiple_indegree), list(multiple_outdegree)
    
    def createNodesList(self):
        nodes_list = {}
        edges_list = set()
        
        for i in self.reads:
            for kmer_index in range(len(i)-self.kmer_len+1):
                edge = i[kmer_index:kmer_index + self.kmer_len]
                edges_list.add(edge)
                edge_prefix = edge[:-1]
                edge_suffix = edge[1:]                
                                    
                nodes_list.setdefault(edge_prefix, Nodes(edge_prefix))
                nodes_list.setdefault(edge_suffix, Nodes(edge_suffix))
                    
        return edges_list, nodes_list

    def dfs(self, current_node, start_node, path, depth = 1, end_index = 0):
        
        path.append(current_node)
        depth += 1
        
        if current_node == start_node or depth > self.bubble_threshold + 1: # To avoid self loop to start node and to control depth
            path.pop()
            depth -= 1  # remove the last node and move up the iteration to find next plausible bubble path
            return path, depth
        
        if current_node in self.multiple_indegree:
            end_index = len(path)-1 # Store the last node having multiple in-degree in the path because we want to get as long path as 
            # possible untill the bubble threshold
        current_obj = self.nodes_list[current_node]
        for next_node in current_obj.neighbors:
            path, depth = self.dfs(next_node, start_node, path, depth, end_index)
            
        if end_index != 0 and current_node in self.multiple_indegree: # Now moving up from dfs keep on storing the paths in the global 
            # path_list for which end_index exists
            node_pair_key = str(path[0]) + "__" + str(path[-1])
            
            if node_pair_key not in self.path_list:
                self.path_list[node_pair_key] = [path[:end_index+1]]
            else:
                self.path_list[node_pair_key].append(path[:end_index+1])
                
        path.pop() # After sotring the plausible bubble path remove last element from the path so that dfs finds another 
        # neighboring path in the branch
        depth -= 1
        return path, depth
            

    def findPossibleBubblePath(self): # To scan all the paths starting from nodes having multiple_outdegree
        for out_node in self.multiple_outdegree:
            out_obj = self.nodes_list[out_node]
            start_node = out_node
            
            for neighbor in out_obj.neighbors:
                path = [out_node]
                self.dfs(neighbor, start_node, path)
                
    def paths_disjoint(self, pair): 
        len_diff = len(set(pair[0]) & set(pair[1]))
        return len_diff
        

    def findBubbles(self):
        bubble_count = 0
        for k,v in self.path_list.items():
            if len(v) > 1:
                for pair in itertools.combinations(v, r=2): # All combinations of length 2
                    if self.paths_disjoint(pair) == 2: # Check if max intersection bet paths is 2, start and end
                        bubble_count += 1
        return bubble_count
                    
    
#    def printNodes(self):
#        for node in self.nodes_list:
#            node_obj = self.nodes_list[node]
#            print("-----------------------------------------------")
#            print(f"Node = {node_obj.node_string}")
#            print(f"neighbors = {node_obj.neighbors}")
#            print(f"in_degree = {node_obj.in_degree}")
#            print(f"out_degree = {node_obj.out_degree}")
            
#    def printPath(self):
#        for path in self.path_list:
#            print("-----------------------------------------------")
#            print(path)
#            print("\n".join(map(str, self.path_list[path])))
        
#if __name__ == "__main__":
def main():
    flowGraph()
    
threading.Thread(target=main).start()
