from collections import deque


class TreeNode:
  def __init__(self, val):
      self.val = val
      self.left, self.right = None, None


def find_successor(root, key):
    # TODO: Write your code here
    q = deque()
    q.append(root)
    nodes_at_level = 0
    while q:
        nodes_at_level = len(q)
        for _ in range(nodes_at_level):
            _node = q.popleft()
            if _node.left: q.append(_node.left)
            if _node.right: q.append(_node.right)
            if _node.val == key: return q.popleft()
    return None


def main():
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left = TreeNode(4);
    root.left.right = TreeNode(5);
  
    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
  
    result = find_successor(root, 9)
    if result:
        print(result.val)
  
    result = find_successor(root, 12)
    if result:
        print(result.val)


main()



'''
Time Complexity - O(N+N)
Space Complexity - O(K)
'''
