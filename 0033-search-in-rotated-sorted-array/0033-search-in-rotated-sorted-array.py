class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def ispossible(l,m,r):
            return nums[m]<target<=nums[r] or (nums[m]>nums[r] and not nums[l]<=target<nums[m])
        
        
        n=len(nums)-1
        l,r=0,n
        while l<r:
            m=(l+r)>>1
            if nums[m]==target:return m
            
            if ispossible(l,m,r):
                l=m+1
            else:
                r=m-1
        return l if nums[l]==target else -1