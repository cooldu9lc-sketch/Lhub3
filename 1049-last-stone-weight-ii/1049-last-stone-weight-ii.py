class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
    
        total = sum(stones)
        target = total // 2
        n = len(stones)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            w = stones[i - 1]
            for s in range(target + 1):
                dp[i][s] = dp[i - 1][s]
                if s >= w:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - w]

        for s in range(target, -1, -1):
            if dp[n][s]:
                return total - 2 * s
        return 0