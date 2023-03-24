# python3


import sys
import threading
#import math

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.D = float('inf')


def ReadTree():
    size = int(input())
#    tree = [Vertex(w) for w in map(int, input().split())]
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
#        a, b = list(map(int, input().split()))
        a, b = map(int, input().split())
        tree[a - 1].children.append(b - 1) 
        tree[b - 1].children.append(a - 1) # Even parent appended in children list of the node
    return tree


def dfs(tree, vertex, parent):
    if tree[vertex].D == float('inf'):
        if (len(tree[vertex].children) == 1 and tree[vertex].children[0] == parent): # If vertex has no children
            tree[vertex].D = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for child in tree[vertex].children:
                if child != parent:
                    for grandchild in tree[child].children:
                        if grandchild != vertex:
                            m1 = m1 + dfs(tree, grandchild, child)

            m0 = 0
            for child in tree[vertex].children:
                if child != parent:
                    m0 = m0 + dfs(tree, child, vertex)
            tree[vertex].D = max(m0, m1)
    return tree[vertex].D


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    
    return dfs(tree, 0, -1)

#if __name__ == "__main__":
#    tree = ReadTree();
#    weight = MaxWeightIndependentTreeSubset(tree);
#    print(weight)
    


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

'''
Implement the algo in the lectures slides. 
There is no parent created for this tree, even parent of the node is included in the children list, while 
iterating the childrens of a node it is checked that the child != parent to avoid iterating over child

Running time is O(T) linear time because adjacency list creation is linear and after it there is just one serious call to dfs algorithm
for each node
'''

