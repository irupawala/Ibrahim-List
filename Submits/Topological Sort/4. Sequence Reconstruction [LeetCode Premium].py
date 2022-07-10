from collections import deque

def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    # a. Initialize the graph
    inDegree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    # b. Build the graph
    for sequence in sequences:
        for i in range(1, len(sequence)):
          parent, child = sequence[i - 1], sequence[i]
          graph[parent].append(child)
          inDegree[child] += 1

    # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
    if len(inDegree) != len(originalSeq):
        return False

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        if len(sources) > 1:
            return False  # more than one sources mean, there is more than one way to reconstruct the sequence
        if originalSeq[len(sortedOrder)] != sources[0]:
            # the next source(or number) is different from the original sequence
            return False

        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
    return len(sortedOrder) == len(originalSeq)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()

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

