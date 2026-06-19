# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recur(node):
            if not node:return 0
            L=recur(node.left)+1
            R=recur(node.right)+1
            return max(L,R)
        return recur(root)