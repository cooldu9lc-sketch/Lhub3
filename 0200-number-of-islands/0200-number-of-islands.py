class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
          
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i==m or j<0 or j==n or grid[i][j]=="0":
                return 0
            grid[i][j]="0"
            return dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j)+dfs(i-1,j)

        res=0
        for i,j in product(range(m),range(n)):
            if grid[i][j]=="1":
                dfs(i,j)
                res+=1
        return res