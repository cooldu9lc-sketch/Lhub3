class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()

       #important to add grid[0][0] as initial time for heap
        heap=[(grid[0][0],0,0)]
     
        while heap:
            time,x,y=heapq.heappop(heap)
            if x==y==n-1:
                return time
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=dx<n and 0<=dy<n and (dx,dy) not in visited:
                    heapq.heappush(heap,(max(time,grid[dx][dy]),dx,dy))
        
        