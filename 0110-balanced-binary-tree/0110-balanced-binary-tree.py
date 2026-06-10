# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def height(node):
            if not node:return 0
            nonlocal res
             
            L=height(node.left) 
            R=height(node.right) 
            if abs(L-R)>1:
                res=False
            return max(L,R)+1
            
        res=True
        height(root)
        return res
        