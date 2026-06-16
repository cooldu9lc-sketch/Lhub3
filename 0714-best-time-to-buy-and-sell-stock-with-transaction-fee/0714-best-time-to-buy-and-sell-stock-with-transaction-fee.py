class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        sold, hold = 0, float('-inf') 

        for price in prices:
            hold,sold = max(hold, sold - price), max(sold, hold + price - fee)
        return max(sold, 0)