class Solution:
    def countSubstrings(self, s: str) -> int:


        n = len(s)
        # Initialize an N x N table with False
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # i must go backwards to ensure inner substrings are calculated first
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # Transition function matching our template
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
                    
        return count