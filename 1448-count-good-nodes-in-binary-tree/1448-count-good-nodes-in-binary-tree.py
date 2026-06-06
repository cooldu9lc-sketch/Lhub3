class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recur(node, maxi=float("-inf")):
            return 0 if not node else int(node.val >= maxi) + recur(node.left, max(maxi, node.val)) + recur(node.right, max(maxi, node.val))
        return recur(root)