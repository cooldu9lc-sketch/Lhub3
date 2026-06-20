# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
      
        vals={node.val for node in nodes}
        self.ans=None

        def recur(node):
            if not node:return 0
            L,R = recur(node.left),recur(node.right)
            if self.ans==None and L+R+ int(node.val in vals)==len(vals):
                self.ans=node
            return L+R+ int(node.val in vals)
        recur(root)
        return self.ans