"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mapp = defaultdict(lambda: Node(0))
        mapp[None]=None
        start = head
        while head:
            mapp[head].val = head.val
            mapp[head].next = mapp[head.next]
            mapp[head].random = mapp[head.random]
            head = head.next



        return mapp[start]