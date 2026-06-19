# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        d={}
        for i,e in enumerate(inorder):
            d[e]=i
            
        def tree(l,r):
            if l>r:
                return None
            val=preorder.pop()
            node=TreeNode(val)
            m=d[val]
            node.left=tree(l,m-1)
            node.right=tree(m+1,r)
            return node
            
            
        
        preorder.reverse()
        return tree(0,len(inorder)-1)
            