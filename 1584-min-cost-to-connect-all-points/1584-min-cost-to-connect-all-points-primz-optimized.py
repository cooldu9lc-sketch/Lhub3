class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance=lambda i,j: abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        n=len(points)
        heap=[(0,0)]
        seen=set()
        dist= [float("inf")] *n

        ## You stil need seen set while using dist array because dist array could get updated within the inner for loop before it is popped.
        ## Seen is exclusively used to check if a node is then popped or not

        res=0
        ##### PRIMS ALGORITHM
        while heap and len(seen)<n:
            weight,idx=heapq.heappop(heap)
            if idx in seen or dist[idx]<weight:continue
            seen.add(idx)
            dist[idx]=weight
            res+=weight
            for i,(x,y) in enumerate(points):
                if i in seen or (next_weight:=distance(idx,i))>dist[i]:continue
                heapq.heappush(heap,(distance(idx,i),i))
        return res

