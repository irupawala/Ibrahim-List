# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:52:01 2022

@author: 1000249643
"""

def organizingLottery(segments, points):
    
    nodes = []
    points_count = dict()
    
    # Append start and end of the segment with left and right
    for s in segments:
        start, end = ["left", s[0]], ["right", s[1]]
        nodes.append(start)
        nodes.append(end)
        
    for p in points:
        points_count[str(p)] = 0
        point = ["point", p]
        nodes.append(point)
        
    # Sorting the nodes with second element
    nodes = sorted(nodes, key = lambda x: x[1])
    
    # Now for each point count the no of lefts and rights it is sorrounded by 
    count = 0    
    for node in nodes:

        if node[0] == "left": count += 1
        if node[0] == "right": count -= 1
        if node[0] == "point": points_count[str(node[1])] += count

    return(points_count.values())    


if __name__ == "__main__":
    s, p = list(map(int, input().split()))
    segments = [(list(map(int, input().split()))) for i in range(s)]
    points = list(map(int, input().split()))

    print(" ".join(map(str, organizingLottery(segments, points))))    


'''

Running time - O(log(s+p)) + s + p          ### Actually it is 2s + 2p

'''