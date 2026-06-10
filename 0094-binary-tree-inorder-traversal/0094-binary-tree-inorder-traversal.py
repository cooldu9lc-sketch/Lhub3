# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        while root:
            if not root.left:
                res.append(root.val)
                root=root.right
            else:
                pre=root.left
                while pre.right!=root and pre.right!=None:
                    pre=pre.right
                if pre.right==root:
                    pre.right=None
                    res.append(root.val)
                    root=root.right
                else:
                    pre.right=root
                    root=root.left
        return res