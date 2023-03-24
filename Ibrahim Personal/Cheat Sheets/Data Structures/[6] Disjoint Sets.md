# Disjoint Sets

* A Disjoint-set data structure supports the following operations: MakeSet(x), Find(x) and Union(x,y).
* To make an efficient implementation represent each set as a rooted tree and use its root as ID of set.
* Use array parent[1...n]: parent[i] is the parent of i, or i if it is the root.
* To make the running time optimal. Use two heuristics: Union by Rank and Path Compression.
* Union by Rank: When merging two trees we hang a shorter one under the root of a taller one. This guarantees height of the tree and that Union and Find works in time at most **O(log2n)**.
* Path Compression: When using Find(x), the algorithm traverses from all nodes in the path from node x to root. In path compression heuristics, we make the parent of all the nodes on this path the root node.
* The Path Compression heuristics guarantees amortized running time of a single operation is **O(log*n)**. For practical values of n, log**n <=5.
* The iterated logarithm of n, log*n, is the number of times the logarithm function needs to be applied to n before the result is less or equal than 1.

![1642823290806](C:\Users\1000249643\AppData\Roaming\Typora\typora-user-images\1642823290806.png)

* Notice that with Path Compression Heuristics Height ≤ Rank, that is rank[i]  is no longer equal to the height of the subtree rooted at i. Still, the height of the subtree rooted at i is at most rank[i] viz rank[i] < rank[parent[i]]

## Time for common Operations

- All Operations work in amortized time **O(log*n)**.

## When to use ?

- Use when groups of different values is to be created and each group needs to be identified by some value. Famous Algo which uses Disjoint sets is Kruskal's Minimal Spanning Tree.

## Python Implementation

```python
class Node:
    def __init__(self, id, parent, rank):
        self.id = id
        self.rank = rank
        self.parent = parent
        self.weight = 1 # Stores the number of elements in this set
        
class Disjointsets:
    def __init__(self, list_nodes):
        self.disjoint_sets = {}      
        for x in set(list_nodes):
            self.disjoint_sets[str(x)] = self.makeset(x)
            
    def makeset(self, x):
        return Node(x, x, 0)
            
    def find(self, x):
        node_x = self.disjoint_sets[str(x)]
        
        # keep on recursively calling find untill root node is not found
        if node_x.parent != x: 
            node_x.parent = self.find(node_x.parent)          
        return node_x.parent # Path Compression Heuristics   
            
    def union(self, u, v):       
        root_u, root_v = self.find(u), self.find(v)  
        if root_u == root_v: # Both have same root hence elements are already in same set 
            return
        
        root_node_u, root_node_v = self.disjoint_sets[str(root_u)], self.disjoint_sets[str(root_v)]     

        if root_node_u.rank < root_node_v.rank: # Union by rank heuristics
            root_node_u.parent = root_v
            root_node_v.weight = root_node_u.weight + root_node_v.weight
            
        else:
            root_node_v.parent = root_u
            root_node_u.weight = root_node_u.weight + root_node_v.weight
            if root_node_u.rank == root_node_v.rank:
                root_node_u.rank += 1       
                
if __name__ == "__main__":
    
    gb = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
    
    nodes_list = []
    for x in gb: nodes_list.extend(x)
    
    D = Disjointsets(nodes_list)    
    for (u, v) in gb:
        D.union(u, v)
```

## Implementation using Dictionary

```python
class Disjointsets:
    def __init__(self, list_nodes):
        self.disjoint_sets = {i:{i} for i in set(list_nodes)}
    
    def length(self):
        return len(self.disjoint_sets)
    
    def Find(self, x):
        keys_list = list(self.disjoint_sets.keys())
        values_list = list(self.disjoint_sets.values())
        
        for index, vertex in enumerate(values_list):
            if x in vertex:
                key = keys_list[values_list.index(vertex)]
                return key            
    
    def Union(self, set_u, set_v):
        key_u, key_v = self.Find(set_u), self.Find(set_v)
        element_union = self.disjoint_sets[key_u].union(self.disjoint_sets[key_v])    
        self.disjoint_sets[key_u] = element_union
        del(self.disjoint_sets[key_v]) 

if __name__ == "__main__":
    
    gb = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
    nodes_list = []
    for x in gb: nodes_list.extend(x)
    
    D = Disjointsets(nodes_list)    
    for (u, v) in gb:
        D.Union(u, v)      
    print(D.length())    
```

## Implementation without Nodes or recursive function

```python 
class Solution:
    def findCircleNum(self, n, isConnected) -> int:
        par = [i for i in range(n)]
        weight = [1] * n
        rank = [0] * n
        
        def find(n1):
            res = n1
            
            while res != par[res]:
                # par[res] = find(par[res]) # path compression heuristics
                par[res] = par[par[res]] # path compression heuristics
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]: #union by rank heuristic
                par[p2] = p1
                weight[p1] += weight[p2]
            else:
                par[p1] = p2
                weight[p2] += weight[p1]
                if rank[p1] == rank[p2]:
                    rank[p2] += 1
            return 1    
        
        total_sets = n
        
        for a,b in edges:
            total_sets -= union(a,b)
            
        return total_sets
  
if __name__ == "__main__":
    S = Solution()
    edges = [[1, 3], [4, 1], [2, 0], [1,2], [1, 5]]
    print(S.findCircleNum(6, edges))
```

## Problems which uses Union Find Algorithm

* https://leetcode.com/problems/redundant-connection/
* https://leetcode.com/problems/number-of-provinces/
* https://leetcode.com/problems/is-graph-bipartite/

## Without Union by Rank Heuristics

```python 
class Solution:
    def isBipartite(self, graph) -> bool:
        #write your code here
        parents = [i for i in range(len(graph))]
        
        def find(n):
            while n != parents[n]:
                parents[n] = parents[parents[n]] # Path Compression Heuristics
                #parents[n] = find(parents[n])
                n = parents[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2: parents[p1] = p2  
        
        for i in range(len(graph)):
            par_i = find(i)
            for j in graph[i]:
                if find(j) == par_i: return False
                union(graph[i][0], j)
                
        #print(parents)
        return True

```

