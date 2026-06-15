class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x))
        curr=intervals[0][1]
        count=0
        for s,e in intervals[1:]:
            if s<curr:
                count+=1
                curr=min(curr,e)
            else:
                curr=e
                
        return count