class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        cash = 0

        for p in prices:
            hold = max(hold, -p)
            cash = max(cash, hold + p)

        return cash