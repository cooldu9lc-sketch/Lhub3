class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        lo=hi=res=nums[0]
        for num in nums[1:]:
            lo,hi=min(lo*num,num,hi*num),max(hi*num,num,lo*num)
            res=max(res,hi)
        return res