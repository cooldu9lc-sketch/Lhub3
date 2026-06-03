class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
   
        d=[inf]*n
        d[src]=0
      
        for i in range(k+1):
            temp=d[:]
            for u,v,w in flights:
                if d[u]!=inf:
                    temp[v]=min(temp[v],d[u]+w)
            d=temp
        return d[dst] if d[dst]!=inf else -1

        ##Bellman Ford

        ### normally for bellman ford , we don't need to use a separate temp array
        ### d[v]=min(d[v],d[u]+w) works in general case for bellman ford
        ## however since we are limited to at most k+1 edges, we want all 
        ## d[v] from the previous iteration only and none from the same iteration