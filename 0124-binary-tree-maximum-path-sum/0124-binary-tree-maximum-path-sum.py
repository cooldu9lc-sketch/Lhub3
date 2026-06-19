# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-inf")

        def recur(node):
            if not node:return 0
            L=recur(node.left)
            R=recur(node.right)
            self.res=max(self.res,node.val+L+R,node.val+L,node.val+R,node.val)
            return max(node.val+L,node.val+R,node.val)
        recur(root)
        return self.res