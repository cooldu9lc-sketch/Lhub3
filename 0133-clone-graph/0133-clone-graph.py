"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return None
        
        mydic=dict()
        def dfs(node):
            if node.val in mydic:
                return mydic[node.val]
            clonenode=mydic.setdefault(node.val,Node(node.val))
            for neigh in node.neighbors:
                clonenode.neighbors.append(dfs(neigh))
            return clonenode
        
        return dfs(node)