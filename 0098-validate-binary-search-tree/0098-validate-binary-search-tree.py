# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack=[(root,-inf,inf)]
        while stack:
            node,l,r=stack.pop()
            if not l<node.val<r:return False

            if node.right:
                stack.append((node.right,node.val,r))
            if node.left:
                stack.append((node.left,l,node.val))
        return True