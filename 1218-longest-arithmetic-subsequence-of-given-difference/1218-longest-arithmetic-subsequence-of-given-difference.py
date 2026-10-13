class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d=defaultdict(int)
        ans=0
        for num in arr:
            d[num]=d[num-difference]+1
            ans=max(ans,d[num])
        return ans

    ## The Solution acts for a subsequence , not Subset
    ## So the order of the elements matters, 
    # and we can only consider elements that appear before the current element in the array.
    ## Thus the solution is correct and efficient
            