class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back=one_back=res=0
        for num in nums:
            one_back,two_back=max(num+two_back,one_back),one_back
        return one_back