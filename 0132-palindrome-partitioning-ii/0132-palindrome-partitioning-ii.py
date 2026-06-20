class Solution:
    def minCut(self, s: str) -> int:
        
        n=len(s)
        # 1. Precompute Palindromes (2D DP)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    
        # 2. Compute Minimum Cuts (1D DP)
        # cuts[i] = max possible cuts is 'i' (cutting every single character)
        cuts = list(range(n)) # Cleaner initialization
        
        for i in range(n):
            # j is the START index of the substring ending at i
            for j in range(i + 1):  ##Notice that j runs till i+1 covering j==i scenario
                if dp[j][i]: # Reads naturally: "If s[j...i] is a palindrome"
                    if j == 0:
                        # The entire prefix s[0...i] is a palindrome
                        cuts[i] = 0 
                    else:
                        # Make a cut right before j. 
                        # Cuts needed = cuts for s[0...j-1] + 1 new cut
                        cuts[i] = min(cuts[i], cuts[j - 1] + 1)
                        
        return cuts[n - 1]
