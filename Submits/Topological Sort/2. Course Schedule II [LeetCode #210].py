LeetCode Link - https://leetcode.com/problems/course-schedule-ii/

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sortedOrder = []
        if numCourses <= 0:
            return False
        
        # a. Initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}  # count of incoming edges
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        
        # b. Build the graph
        for prerequisite in prerequisites:
            child, parent  = prerequisite[0], prerequisite[1]
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
        if len(sortedOrder) != numCourses:
            return []

        return sortedOrder             

'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|) for adjacency list
'''
