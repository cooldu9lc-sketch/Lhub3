class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:return 0
        curr_max=next_max=res=0
        for i,num in enumerate(nums):
            next_max=max(next_max,i+num)
            if next_max>=n-1:
                return res+1
            if curr_max==i:
                res+=1
                curr_max=next_max
        return res
