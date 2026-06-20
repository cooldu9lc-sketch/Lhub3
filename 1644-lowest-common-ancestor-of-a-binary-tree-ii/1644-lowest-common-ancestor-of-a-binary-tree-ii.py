# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         
        def recur(node):
            if not node:
                return False
            L=recur(node.left)
            R=recur(node.right)
            if (L and R) or ((L or R) and (node==p or node==q)):
                self.ans=node
                return
            return L or R or node==p or node==q


        self.ans=None
        recur(root)
        return self.ans