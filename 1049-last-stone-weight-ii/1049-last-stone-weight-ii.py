class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
    
        total = sum(stones)
        target = total // 2
        n = len(stones)

        dp = [False] * (target + 1) 
        dp[0] = True

        for num in stones:
            for w in range(target ,num-1,-1):
               dp[w] = dp[w] or dp[w - num]
         ## find Max value of s such that dp[s] is True and s <= target
        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
        return 0