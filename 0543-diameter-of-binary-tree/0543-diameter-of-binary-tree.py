# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res= float("-inf")
        def recur(node=0):
            if not node: return 0
            L = recur(node.left)
            R = recur(node.right)
            self.res= max(self.res,L+R)
            return max(L,R) +1
        recur(root)
        
        return self.res