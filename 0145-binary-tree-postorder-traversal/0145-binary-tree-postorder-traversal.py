# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack, output = [root,], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)

        return output[::-1]