class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n=len(rooms),len(rooms[0])
        wall,gate,empty=-1,0,2147483647
        q=deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==gate:
                    q.append((0,i,j))
                    

        while q:
            dist,r,c=q.popleft()
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<m and 0<=nc<n and rooms[nr][nc]==empty:
                    rooms[nr][nc]=dist+1
                    q.append((dist+1,nr,nc))
        