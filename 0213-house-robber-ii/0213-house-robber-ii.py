class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        
        def rob(arr):
            two_back=one_back=res=0
            for num in arr:
                one_back,two_back=max(num+two_back,one_back),one_back
            return one_back
        return max(rob(nums[:-1]),rob(nums[1:]))