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
        def preorder(node):
            return [str(node.val)] + preorder(node.left)+preorder(node.right) if node else ["#"]
        return " ".join(preorder(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals= iter(data.split())
        def recur():
            val= next(vals)
            if val=="#":return None
            node=TreeNode(int(val))
            node.left=recur()
            node.right=recur()
            return node
        return recur()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))