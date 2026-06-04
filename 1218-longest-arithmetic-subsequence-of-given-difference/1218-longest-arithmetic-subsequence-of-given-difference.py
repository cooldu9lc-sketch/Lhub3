class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d=defaultdict(int)
        ans=0
        for num in arr:
            d[num]=d[num-difference]+1
            ans=max(ans,d[num])
        return ans
            