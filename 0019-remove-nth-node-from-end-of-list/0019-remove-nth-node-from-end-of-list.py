class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        # Advances first pointer from Dummy node  so that the gap between first and second is n nodes apart
        for i in range(n + 1): # Loop runs n+1 ties from Auxilary
            first = first.next # First is at node n+1 here
        # Move first to the end, maintaining the gap
        # In the while loop , first positions are n+2,n+3,n+4
        # while second positions are 1,2,3
        ## so first and second positions are always at an n-1 difference
        ###AFter the end of while loop
        #### second is at L+1-n-1= L-nth Node
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next