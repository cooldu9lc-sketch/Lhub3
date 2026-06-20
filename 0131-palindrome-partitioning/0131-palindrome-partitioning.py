class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        # 1. Precompute the DP table bottom-up
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    
        res = []
        
        # 2. Backtrack using the precomputed table
        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                if dp[start][end]: # O(1) lookup
                    path.append(s[start:end + 1])
                    dfs(end + 1, path)
                    path.pop()
                    
        dfs(0, [])
        return res