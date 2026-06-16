class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold = float('-inf')
        sold = 0
        rest = 0

        for p in prices:
            prev_hold = hold
            prev_sold = sold
            hold = max(hold,rest - p)
            sold = prev_hold + p
            rest = max(rest,prev_sold)

        return max(rest, sold)
       