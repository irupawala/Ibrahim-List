#Uses python3

# Coursera Data Structures and Algorithms - Algorithms of Graph, Week5, Problem 2 Clustering

'''
To solve this problem apply Kruskal's Algo and keep on adding min length edges till k clusters (sets)
are created. After k sets has been made the min distance calculated between any two sets is the 
the largest possible value of 𝑑 such that the given points can be partitioned into 𝑘 non-empty subsets
in such a way that the distance between any two points from different subsets is at least 𝑑.

Running Time - T(CalculateWeight) + T(MakeSet) + |E|(T(Find)) + |V|T(Union) =~ O(|V|^2) + O(|V|) + O((|E|+|V|)log|V|) with Disjoint sets
Running Time - T(CalculateWeight) + T(MakeSet) + |E|(T(Find)) + |V|T(Union) =~ O(|V|^2) + O(|V|) + O((|E|+|V|)(1)) with Dict Disjoint sets 
 
'''
