"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:return None
        copy = defaultdict(lambda: Node())
        #copy[None]=None
        def clone(node):
            if node in copy:
                return copy[node]
            copy[node].val=node.val
            for neighbour in node.neighbors:
                copy[node].neighbors.append(clone(neighbour))
            
            return copy[node]


        return clone(node)