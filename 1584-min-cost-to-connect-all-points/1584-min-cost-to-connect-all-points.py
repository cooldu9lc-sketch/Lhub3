class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance=lambda i,j: abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        n=len(points)
        heap=[(0,0)]
        seen=set()
        vertices=res=0
        ##### PRIMS ALGORITHM
        while heap and vertices<n:
            cost,idx=heapq.heappop(heap)
            if idx in seen:continue
            seen.add(idx)
            res+=cost
            vertices+=1
            for i,(x,y) in enumerate(points):
                if i in seen:continue
                heapq.heappush(heap,(distance(idx,i),i))
        return res

