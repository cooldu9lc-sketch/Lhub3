class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:return True
        intervals.sort()
        s,e=intervals[0]
        for x,y in intervals[1:]:
            if x<e:return False
            e=y
        return True