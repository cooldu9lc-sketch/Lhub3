class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        max_len=0
        def dfs(x, y, prev):
            nonlocal max_len
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= prev: 
                return 0
            #if already calculated,return
            if (x,y) in table:
                return table[(x,y)]
            path = 1 + max(dfs(x+1, y, matrix[x][y]), dfs(x-1, y, matrix[x][y]), dfs(x, y+1, matrix[x][y]), dfs(x, y-1, matrix[x][y]))
            max_len = max(max_len, path)
            #memoisation
            table[(x,y)] = path
            return path
        
        
        table = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, float("-inf"))
        return max_len
        