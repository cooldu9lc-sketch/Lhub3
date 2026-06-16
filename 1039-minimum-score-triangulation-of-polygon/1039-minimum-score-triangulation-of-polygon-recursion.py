from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            minnum = float("Inf")
            for k in range(left+1, right):
                minnum = min(minnum, values[left]*values[right]*values[k] + dfs(left, k) + dfs(k, right))
            return minnum
        return dfs(0, len(values) - 1)