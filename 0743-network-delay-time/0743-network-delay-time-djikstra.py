class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float("inf")]*n for _ in range(n)] 
        #dist = [[float("inf") for i in range(n)] for j in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u,v,w in times:
            dist[u-1][v-1] = w
        for p in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][p] + dist[p][j])
        if max(dist[k-1]) < float("inf"):
            return max(dist[k-1])
        else:
            return -1