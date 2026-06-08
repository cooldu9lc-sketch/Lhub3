class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n=len(grid),len(grid[0])
        
        q =collections.deque([])
        res=fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1
       
        while fresh and q:
            x,y,c=q.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    fresh-=1
                    grid[nx][ny]=2
                    q.append((nx,ny,c+1))
                    res=c+1
        return res if not fresh else -1