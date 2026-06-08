class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:continue
            target=-nums[i]
            j,k=i+1,n-1
            while j<k:
                if nums[j]+nums[k]==target:
                    res.append([nums[i],nums[j],nums[k]])
                    p,q=j,k
                    while p<=k and nums[p]==nums[j]:
                        p+=1
                    while q>=p and nums[q]==nums[k]:
                        q-=1
                    j,k=p,q
                elif nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1

        return res
                    