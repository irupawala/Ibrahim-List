# python3
# import sys


class SuffixTreeNode():
    def __init__(self, children, parent, stringDepth, edgeStart, edgeEnd):
        self.children = children
        self.parent = parent
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd
        
    def read(self):
        return(self.children, self.parent, self.stringDepth, self.edgeStart, self.edgeEnd)
        

def CreateNewLeaf(node, S, suffix):
    leaf = SuffixTreeNode(
            children = {},
            parent = node,
            stringDepth = len(S) - suffix,
            edgeStart = suffix + node.stringDepth,
            edgeEnd = len(S))
    
    node.children[S[leaf.edgeStart]] = leaf
    return leaf


def BreakEdge(node, S, start, offset):
    startChar = S[start]
    midChar = S[start + offset]
    midNode = SuffixTreeNode(
            children = {},
            parent = node, 
            stringDepth = node.stringDepth + offset,
            edgeStart = start,
            edgeEnd = start + offset)
    midNode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midNode
    node.children[startChar].edgeStart += offset
    node.children[startChar] = midNode
    return midNode

def suffix_array_to_suffix_tree(S, order, lcpArray):
    

    # Implement this function yourself
    root = SuffixTreeNode(
            children = {},
            parent = None,
            stringDepth = 0,
            edgeStart = -1, 
            edgeEnd = -1           
            )
    
#    print(root.read())
    
    
    
    lcpPrev = 0
    curNode = root
    for i in range (len(S)):
        suffix = order[i]
        while curNode.stringDepth > lcpPrev:
            curNode = curNode.parent
        if curNode.stringDepth == lcpPrev:
            curNode = CreateNewLeaf(curNode, S, suffix)
        else:
            edgeStart = order[i-1] + curNode.stringDepth
            offset = lcpPrev - curNode.stringDepth
            midNode = BreakEdge(curNode, S, edgeStart, offset)
            curNode = CreateNewLeaf(midNode, S, suffix)
        if i < len(S) - 1:
            lcpPrev = lcpArray[i]
                        
    print(list(root.children.keys()))
    
#    for i in root.children:
#        if i != {}:
#            pass 
#        else:
            
            
#    return tree
    

if __name__ == '__main__':
#    text = "ababaa$"
#    sa = [6, 5, 4, 2, 0, 3, 1]
#    lcp = [0, 1, 1, 3, 0, 2]      

#    text = "A$"
#    sa = [1, 0]
#    lcp = [0]
    
    text = "AAA$"
    sa = [3, 2, 1, 0]
    lcp = [0, 1, 2]    
    
    
    print(text)
    suffix_array_to_suffix_tree(text, sa, lcp)
    
#    tree = suffix_array_to_suffix_tree(text, sa, lcp)
    
#    tree = {"$": (1, 1, 2), "A$": (0, 0, 2)}
#    
#    stack = [(0, 0)]
#    result_edges = []
#    while len(stack) > 0:
#      (node, edge_index) = stack[-1]
#      stack.pop()
#      if not node in tree:
#        continue
#      edges = tree[node]
#      if edge_index + 1 < len(edges):
#        stack.append((node, edge_index + 1))
#      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
#      stack.append((edges[edge_index][0], 0))
    