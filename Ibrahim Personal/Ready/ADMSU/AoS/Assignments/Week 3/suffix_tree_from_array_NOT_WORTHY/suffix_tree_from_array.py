# python3
#import sys

'''
def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    tree = {}
    # Implement this function yourself
    return tree
'''    
    
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
    
    root = SuffixTreeNode(
            children = {},
            parent = None,
            stringDepth = 0,
            edgeStart = -1, 
            edgeEnd = -1           
            )
    
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
                        
    return root   
            
#    return tree
    


if __name__ == '__main__':
#    text = sys.stdin.readline().strip()
#    sa = list(map(int, sys.stdin.readline().strip().split()))
#    lcp = list(map(int, sys.stdin.readline().strip().split()))
    
#    text = input().strip()
#    sa = list(map(int, input().strip().split()))
#    lcp = list(map(int, input().strip().split()))    
    
    text = "ababaa$"
    sa = [6, 5, 4, 2, 0, 3, 1]
    lcp = [0, 1, 1, 3, 0, 2]      
    
    print(text)
    
    """
    This code is incomplete it has been implemented from the algorithm given in lecture slides however it is not printing a tree as 
    per the instructions given in this lecture. It is having root node with the entire tree developed. Analyze on pythontutor.
    """
    
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    
#    tree = suffix_array_to_suffix_tree(text, sa, lcp)
    suffix_array_to_suffix_tree(text, sa, lcp)
    
    
    
    
    
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    
    '''
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
    '''