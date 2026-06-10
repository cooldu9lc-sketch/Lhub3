class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        res=-inf
        for num in nums:
            curr=max(num+curr,num)
            res=max(res,curr)
        return res

        