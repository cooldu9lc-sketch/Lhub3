"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen=set()
        while p!=None:
            seen.add(p.val)
            p=p.parent
        while q.val not in seen:
            q=q.parent
        return q