class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph=collections.defaultdict(list)
        for x,y,cost in connections:
            graph[x].append((y,cost))
            graph[y].append((x,cost))
        
        heap=[(0,1)]
        seen=defaultdict(lambda:float("inf"))
        while heap:
            cost,city=heapq.heappop(heap)
            
            if seen[city]>cost:
                seen[city]=cost
                for nei,c in graph[city]:
                    if nei not in seen:
                        heapq.heappush(heap,(c,nei))
        return -1 if len(seen)<n  else sum(seen[i] for i in range(1,n+1))
        ##No Need for both seen set and dist map.
        ## One can function as both