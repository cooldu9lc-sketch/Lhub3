# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node=root
        mini,maxi = min(p.val,q.val),max(p.val,q.val)
        while node:
            if mini<=node.val<=maxi: #or node.val==mini or node.val==maxi:
                return node
            elif maxi<node.val:
                node=node.left
            else:
                node=node.right
            
