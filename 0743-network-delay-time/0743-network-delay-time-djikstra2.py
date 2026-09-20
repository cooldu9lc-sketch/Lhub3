class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float("inf")]*n
        heap=[(0,k-1)]
        edges=collections.defaultdict(list)
        for x,y,z in times:
            edges[x-1].append((y-1,z))
        while heap:
            cost,node,=heapq.heappop(heap)
            if dist[node]>cost:
                dist[node]=cost
                for (v,w) in edges[node]:
                    heapq.heappush(heap,(w+cost,v))
        if max(dist) < float("inf"):
            return max(dist)
        else:
            return -1
        