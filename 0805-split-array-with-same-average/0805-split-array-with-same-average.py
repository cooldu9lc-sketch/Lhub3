class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n, S = len(nums), sum(nums)
        if n == 1: 
            return False
            
        # 1. Mathematical Pruning: Check if a valid length K is even possible
        if not any((S * k) % n == 0 for k in range(1, n // 2 + 1)):
            return False
            
        # dp[k] stores a set of all possible sums formed by exactly 'k' elements
        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)
        
        # 2. Populate the DP Table
        for num in nums:
            # We iterate backwards to prevent using the same 'num' multiple times in one path
            for k in range(n // 2, 0, -1):
                for prev_sum in dp[k - 1]:
                    dp[k].add(prev_sum + num)
                    
        # 3. Final Verification
        for k in range(1, n // 2 + 1):
            if (S * k) % n == 0 and (S * k) // n in dp[k]:
                return True
                
        return False