class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        endheap=[]

        for s,e in intervals:
            if endheap and endheap[0]<=s:
                heappop(endheap)
            heappush(endheap,e)
        return len(endheap)