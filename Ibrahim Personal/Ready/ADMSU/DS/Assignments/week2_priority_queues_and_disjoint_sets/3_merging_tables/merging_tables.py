# python3

'''
Time Complexity - O(m*logn)
To solve this problem merge by Union by rank heuristics and IGNORE the merge order given in input queries

'''

# find method of Disjoint Sets to find the actualParent
def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table] # Path Compression Heuristics

# Union method of Disjoint Sets to merge the trees
def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    lineRoot = 0

    if realDestination == realSource:
        return

    if rank[realDestination] < rank[realSource]: # Union by rank heuristics
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lineRoot = lines[realSource]
        lines[realDestination] = 0
        
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lineRoot = lines[realDestination]
        lines[realSource] = 0     
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1        

    if lineRoot > ans[0]:
        ans[0] = lineRoot


if __name__ == "__main__":
    n, m = map(int, input().split())
    lines = list(map(int, input().split()))
    
    rank = [1] * n
    parent = list(range(0, n))
    ans = [max(lines)]

    for i in range(m):
        destination, source = map(int, input().split())
        merge(destination - 1, source - 1)
        print(ans[0])
