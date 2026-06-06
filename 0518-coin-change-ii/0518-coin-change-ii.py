class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0] * (amount+1)
        dp[0]=1
        
        
        for coin in coins:
            for val in range(coin,amount+1):
                dp[val] += dp[val-coin]                  
               
        print(dp)
        return dp[-1]