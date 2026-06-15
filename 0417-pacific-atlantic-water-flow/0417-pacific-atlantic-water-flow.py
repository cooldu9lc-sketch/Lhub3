class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i,j,prev,res):
            if i<0 or i>=m  or j<0 or j>=n or heights[i][j]<prev or (i,j) in res:
                return

            res.add((i,j))
            dfs(i+1,j,heights[i][j],res)
            dfs(i-1,j,heights[i][j],res)
            dfs(i,j+1,heights[i][j],res)
            dfs(i,j-1,heights[i][j],res)

        pacific, atlantic = set(),set()
        m,n=len(heights),len(heights[0])
        for j in range(n):
            dfs(0,j,-inf,pacific)
            dfs(m-1,j,-inf,atlantic)
        for i in range(m):
            dfs(i,0,-inf,pacific)
            dfs(i,n-1,-inf,atlantic)
        
        return list(pacific & atlantic)