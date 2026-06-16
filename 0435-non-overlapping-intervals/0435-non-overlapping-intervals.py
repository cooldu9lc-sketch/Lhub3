class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x))
        print(intervals)
        curr=-inf
        count=0
        for s,e in intervals:
            if s<curr:
                count+=1
                curr=min(curr,e)
            else:
                curr = e
        return count

        return count