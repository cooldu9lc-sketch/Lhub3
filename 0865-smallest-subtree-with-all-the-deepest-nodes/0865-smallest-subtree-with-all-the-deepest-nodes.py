# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.max_depth=0
        self.lca=root
        def dfs(node,depth):
            self.max_depth=max(self.max_depth,depth)
            if not node:return depth
            L=dfs(node.left,depth+1)
            R=dfs(node.right,depth+1)
            if L==R==self.max_depth:
                self.lca=node
            return max(L,R)
        dfs(root,0)
        return self.lca