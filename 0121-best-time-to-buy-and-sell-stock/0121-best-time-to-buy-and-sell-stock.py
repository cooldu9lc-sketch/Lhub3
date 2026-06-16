class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low=math.inf
        res=0
        for price in prices:
            if price<=low:
                low=price
            else:
                res=max(res,price-low)
        return res