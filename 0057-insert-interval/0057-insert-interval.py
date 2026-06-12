class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
       
        idx= bisect.bisect(intervals,newInterval)
        #left=idx-1
        res=[]
        if idx>0:
            res=intervals[:idx]
            if newInterval[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],newInterval[1])
            else:
                res.append(newInterval)
        else:
            res.append(newInterval)
        for i in range(idx,len(intervals)):
            ns,ne=intervals[i]
            if ns<=res[-1][1]:
                res[-1][1]=max(res[-1][1],ne)
            else:
                res.append([ns,ne])
        return res