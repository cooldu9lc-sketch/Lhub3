"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        dic={}
        def recur(node):
            if not node:return None
            if node.val in dic:
                return dic[node.val]
            clone=Node(node.val)
            dic[node.val]=clone
            for child in node.neighbors:
                clone.neighbors.append(recur(child))
            return clone
        
        return recur(node)