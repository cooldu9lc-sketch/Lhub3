class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res=0
        endTime=-inf
        for s,e in points:
            if s>endTime:
                endTime=e
                res+=1
        return res
            