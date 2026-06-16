class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """res=0
        low=math.inf
        for price in prices:
            if price>low:
                res+=price-low
            low=price
        return res"""

        hold = float('-inf')
        cash = 0

        for p in prices:
            old_hold = hold

            hold = max(hold,cash - p)

            cash = max(cash,old_hold + p)

        return cash