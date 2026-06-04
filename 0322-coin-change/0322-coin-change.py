class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        if amount==0:return 0
        dp= [float("inf")]*(amount+1)
        dp[0]=0
        res = float("inf")
        coins.sort()

        for val in range(1,amount+1):
            for coin in coins:
                if val-coin>=0:
                  dp[val]=min(dp[val],dp[val-coin]+1)
            
                 
        return dp[-1] if dp[-1]!=float("inf") else -1