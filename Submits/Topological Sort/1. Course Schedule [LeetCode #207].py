LeetCode Link - https://leetcode.com/problems/course-schedule/

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        if numCourses <= 0:
            return False
        
        # a. Initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}  # count of incoming edges
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        
        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            inDegree[child] += 1  # increment child's inDegree     

            
        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)            

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)                
                
        # if sortedOrder doesn't contain all numCourses, there is a cyclic dependency between numCourses, therefore, we
        # will not be able to schedule all numCourses
        return len(sortedOrder) == numCourses                

'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|) for adjacency list
'''


# NeetCode DFS Solution
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        visited = [False for i in range(numCourses)] # To not revisit the node
        
        # populate adjaceny list
        for lst in prerequisites:
            adj_list[lst[0]].append(lst[1])        
        
        def dfs(i, traversal_list):            
            if i in traversal_list:
                return False
            
            visited[i] = True
            
            traversal_list.append(i)            
            for j in adj_list[i]:
                if not dfs(j, traversal_list): return False            
            traversal_list.remove(i)
            
            adj_list[i] = [] # This line is super-crucial. After visiting the node we want to make its adjacency list empty so that we 
            # do not have revisit all of its neighbors again because we have checeked once that there is no loop ending on this node.
            # this one-line plays a crucial role in passing the time-complexity
            return True
        
        for i in range(numCourses):
            traversal_list = []
            if not visited[i]:
                if not dfs(i, traversal_list): return False
  
        return True        
'''


'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|) for adjacency list
'''
