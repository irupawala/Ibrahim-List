# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder_list = []
        
        def PreOrder(root):
            if root is None: 
                self.preorder_list.append("N")
                return 
            
            self.preorder_list.append(str(root.val))
            PreOrder(root.left)   
            PreOrder(root.right)
            
        PreOrder(root)
        preorder_str = "$".join(map(str, self.preorder_list))
        #print(preorder_str)
        return preorder_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        serialized_list_str = data.split("$")
        #print(serialized_list_str)
        self.i = 0
        
        def preOrderTraversal():
            if serialized_list_str[self.i] == "N":
                self.i += 1
                return 

            root = TreeNode(int(serialized_list_str[self.i]))
            self.i += 1
            root.left = preOrderTraversal()
            root.right = preOrderTraversal()
            return root
        
        return preOrderTraversal()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


'''
Time Complexity - O(N)
Space Complexity - O(N)
'''