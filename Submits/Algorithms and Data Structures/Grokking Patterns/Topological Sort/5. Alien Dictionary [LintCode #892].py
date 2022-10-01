LintCode Link - https://www.lintcode.com/problem/892/

##############################     BFS SOLUTIONS      ############################

from collections import deque

from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here

        if len(words) == 0:
            return ""

        # a. Initialize the graph
        inDegree = {}  # count of incoming edges
        graph = {}  # adjacency list graph
        for word in words:
            for character in word:
                inDegree[character] = 0
                graph[character] = []

        # b. Build the graph
        for i in range(0, len(words)-1):
            # find ordering of characters from adjacent words
            w1, w2 = words[i], words[i + 1]
            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if parent != child:  # if the two characters are different
                    # put the child into it's parent's list
                    graph[parent].append(child)
                    inDegree[child] += 1  # increment child's inDegree
                    break  # only the first different character between the two words will help us find the order

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
        # will not be able to find the correct ordering of the characters
        if len(sortedOrder) != len(inDegree):
            return ""

        return ''.join(sortedOrder)

##############################     DFS SOLUTIONS      ############################

from collections import deque

from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} 
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
      
'''
Time Complexity 
In step ‘d’, each task can become a source only once and each edge (a rule) will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E)
O(V+E), where ‘V’ is the total number of different characters and ‘E’ is the total number of the rules in the alien language. 
Since, at most, each pair of words can give us one rule, therefore, we can conclude that the upper bound for the rules is O(N)
where ‘N’ is the number of words in the input. So, we can say that the time complexity of our algorithm is O(V+N).

Space Complexity
The space complexity will be O(V+N), since we are storing all of the rules for each character in an adjacency list.
'''
