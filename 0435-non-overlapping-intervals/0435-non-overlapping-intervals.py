class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        curr=-inf
        count=0
        for s,e in intervals:
            if s<curr:
                count+=1
            else:
                curr=e
        return count