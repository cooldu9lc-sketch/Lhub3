class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g=defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
        heap=[(0,k)]
        seen=set()
        res=-inf
        while heap:
            cost,node=heapq.heappop(heap)
            if node not in seen:
                res=max(res,cost)
                seen.add(node)
                for v,w in g[node]:
                    if v not in seen:
                        heapq.heappush(heap,(cost+w,v))
        return res if len(seen)==n else -1 