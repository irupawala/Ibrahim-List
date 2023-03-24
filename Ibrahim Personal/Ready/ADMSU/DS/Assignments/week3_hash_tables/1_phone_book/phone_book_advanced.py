# python3

'''
Running time is O(1)
Space Complexity - O(n)
'''


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

    def access(self):
        print(f"type = {self.type}")
        print(f"number = {self.number}")
        print(f"name = {self.name}")
        
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

#def read_queries():
#    direct_addressing_table = [None] * 10000000
#    n = int(input())
#    for i in range(n) :
#        q = Query(input().split()) 
#        print(q.access())
#
#    return 0    
    

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    direct_addressing_table = [None] * 10000000
    result = []

    for cur_query in queries:
#        print(cur_query.type)
        if cur_query.type == 'add':            
            direct_addressing_table[cur_query.number] = cur_query.name
#            print(direct_addressing_table[cur_query.number])

        elif cur_query.type == 'del':
            direct_addressing_table[cur_query.number] = None
            
        else:
#            print(direct_addressing_table[cur_query.number])
            if direct_addressing_table[cur_query.number] == None:
                response = 'not found'
            else:
                response = direct_addressing_table[cur_query.number]
            result.append(response)            
            
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
#    process_queries(read_queries())
#    read_queries()
    
    

































###############################################################################
################  Example to create list of objeccts  #########################
'''    
    
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:44:58 2020

@author: 1000249643
"""

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
            
    def access(self):
        print(f"type = {self.type}")
        print(f"number = {self.number}")
        print(f"name = {self.name}")
        

if __name__ == '__main__':
    n = int(input()) # give input ""add 911 police"" when prompted
    k = [Query(input().split()) for i in range(n)] # Notice that split creates a list and also a list of all the inputs is created 
    # hence in the end the list will be something like this [['add', '911', 'police'], ['add', '100', 'mumbai_police']]
    print(k[0].access())

'''    
###############################################################################    