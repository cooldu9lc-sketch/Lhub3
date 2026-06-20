class Solution:
    def minCut(self, s: str) -> int:
        
        n=len(s)
        # 1. Precompute Palindromes (2D DP)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    
        # 2. Compute Minimum Cuts (1D DP)
        # cuts[i] = max possible cuts is 'i' (cutting every single character)
        cuts = [i for i in range(n)] 
        
        for end in range(n):
            if dp[0][end]:
                cuts[end]=0
            else:
                for start in range(end):
                    if dp[start+1][end]:
                        cuts[end] = min(cuts[end], cuts[start] + 1)
                        
        return cuts[n - 1]
       
