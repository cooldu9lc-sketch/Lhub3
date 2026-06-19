# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recur(p,q):
            if p==None or  q==None:
                return p==q
            return p.val==q.val and recur(p.left,q.left) and recur(p.right,q.right)
        return recur(p,q)