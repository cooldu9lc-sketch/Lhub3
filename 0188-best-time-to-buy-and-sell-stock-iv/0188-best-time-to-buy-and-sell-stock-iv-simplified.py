class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
       
        states = [0] + [float('-inf')] * (2*k) 
       
 
        for p in prices:
            for j in range(k):
                states[2*j+1] = max(states[2*j+1], states[2*j]-p)
                states[2*j+2] =   max(states[2*j+2], states[2*j+1]+p)
        
        return max(0, states[-1])