# python3


import sys
import threading
from collections import deque

dfs_stack = deque()
#import math

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(11000000) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

class Nodes():
    
    def __init__(self, u):
        self.index = u
        self.value = -1 # the value the vertex becomes in the CNF when satisfied
        
        self.neighbors = []
        # tarjan-specific variables
        self.ids = None # None for UNVISITED, serves two purpose 1. to check ifVisted 2. to keep ids of node 
        self.low = 0
        self.onStack = False
      

class circuitDesign():
    
    def __init__(self, n, m, clauses):
        
        self.n, self.m = n, m
        self.clauses = clauses
        
        self.nodes_dict = {} # Stores the graph as adjacency list.
        # for each vertex stores neighbors
        self.createNodesList()    
        self.implicationGraph()
        
        self.tarjans() # Finds SCCs
        self.printResults()
        
    
    def createNodesList(self):
        
        for i in range(1, self.n+1):
            self.nodes_dict.setdefault(i, Nodes(i))
            self.nodes_dict.setdefault(-i, Nodes(-i))
                  
    def implicationGraph(self):
        
        for clause in self.clauses:
            
            if len(clause) == 1:
                l = clause[0]
                self.nodes_dict[-l].neighbors.append(l)
            
            if len(clause) == 2:
                l1 = clause[0]
                l2 = clause[1]               
                # -l1 --> l2
                self.nodes_dict[-l1].neighbors.append(l2)              
                # -l2 --> l1
                self.nodes_dict[-l2].neighbors.append(l1)                  
            
    def tarjans(self):
        self.id = 0 # Used to give each node and Id
        self.connected_comp = 0 # Used to count number of SCCs found        
        self.scc_list = []
        
        for node in self.nodes_dict:
            node_obj = self.nodes_dict[node]
            ids = node_obj.ids
            
            if ids == None:
                self.dfs(self.nodes_dict[node])                
                
#        print(f"connected_comp = {self.connected_comp}")
#        print(f"scc_list = {self.scc_list}")    


    def dfs(self, at_object):
        dfs_stack.append(at_object)
        self.id += 1

        at_object.onStack = True
        at_object.ids = self.id
        at_object.low = self.id
        
        # Visit all neighbors and min low-link on callback            
        for to_index in at_object.neighbors:
            to_object = self.nodes_dict[to_index]
            if to_object.ids == None:
                self.dfs(to_object)
            if to_object.onStack:
                at_object.low = min(at_object.low, to_object.low)                
            
        # After having visited all the neighbors of 'at_index'
        # If we're at the start of a SCC empty the stack 
        # untill we're back to the start of the SCC.
        
        if at_object.ids == at_object.low :
            scc = set()
#            print(f"dfs_stack = {dfs_stack}")
            while len(dfs_stack) != 0:
                node_obj = dfs_stack.pop()
                scc.add(node_obj.index)
                              
                node_obj.onStack = False
                node_obj.low = at_object.ids

                if node_obj == at_object:
                    self.scc_list.append(scc)
                    break
                
            self.connected_comp += 1

        
    
    def printResults(self):
        
        isSatisfied = True
        for scc in self.scc_list:
            root = list(scc)[-1]
            if -root in scc:
                isSatisfied = False
                break
        
        if isSatisfied == True:            
            result = [None] * (self.n)        
            for scc in self.scc_list:
                for literal in scc:
                    if None not in result:
                        break
                    index = abs(literal)-1
                    if result[index] == None:
                        result[index] = literal
                        self.nodes_dict[literal].value = 1
                        self.nodes_dict[-literal].value = 0

        if isSatisfied is False:
            print("UNSATISFIABLE")
            
        else:
            print("SATISFIABLE")
            print(" ".join(map(str, result)))
            
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
    
    circuitDesign(n, m, clauses) 


#############################################################################################################

#if __name__ == "__main__":
def main():  
    
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
#    data = list(map(int, input().split()))   
   
#    data = [3, 3, 1, -3, -1, 2, -2, -3]
#    data = [4, 5, 1, 2, 2, 3, 3, 4, -1, -3, -2, -4]
#    data = [8, 12, 1, 4, -2, 5, 3, 7, 2, -5, -8, -2, 3, -1, 4, -3, 5, -4, -3, -7, 6, 7, 1, 7, -7, -1]

#    input = sys.stdin.read()
#    data = list(map(int, input.split()))       
##    data = list(map(int, input().split()))       
#    n = int(data[0])
#    m = int(data[1])
#    input_2 = data[2:]
#    clauses = list(zip(input_2[0:(2 * m):2], input_2[1:(2 * m):2]))        
    circuitDesign(n, m, clauses)
    
#    test()

threading.Thread(target=main).start()               