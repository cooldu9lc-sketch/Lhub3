class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [1]
        for i in range(1, n):
            if dp[-1] == 0 or obstacleGrid[0][i] == 1:
                dp.append(0)
            else:
                dp.append(1)
        for i in range(1, m):
            if dp[0]==0 or obstacleGrid[i][0]:
                dp[0] = 0
            for col in range(1, n):
                if obstacleGrid[i][col] == 1:
                    dp[col] = 0
                else:
                    dp[col] = dp[col] + dp[col - 1]
        return dp[-1]
