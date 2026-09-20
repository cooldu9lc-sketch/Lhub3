class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d=[inf]*n
        d[k-1]=0
        for i in range(n-1):
            for u,v,w in times:
                d[v]=min(d[v],d[u]+w)
           
        return max(d) if max(d)!=inf else -1