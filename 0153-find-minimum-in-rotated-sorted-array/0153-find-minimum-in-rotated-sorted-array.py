class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def ispossible(l,m,r,target):
            return nums[m]<target<=nums[r] or (nums[m]>nums[r] and not nums[l]<=target<nums[m])
        
        
        n=len(nums)-1
        l,r=0,n
        while l<r:
            m=(l+r)>>1
            target = nums[m]
            
            if ispossible(l,m,r,target):
                l=m+1
            else:
                r=m
        return nums[l]