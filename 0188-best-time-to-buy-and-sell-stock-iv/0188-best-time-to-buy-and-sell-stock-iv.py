class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
       
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t],sell[t - 1] - p)

                sell[t] = max(sell[t],buy[t] + p)

        return sell[k]
        
       