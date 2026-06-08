# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = curr = ListNode()
        heap=[]

        for i,l in enumerate(lists):
            if l:
                heappush(heap,(l.val,i,l))
        while heap:
            val,idx,node = heappop(heap)
            curr.next=node
            curr = node
            if node.next:
                node=node.next
                heappush(heap,(node.val,idx,node))
        return dummy.next