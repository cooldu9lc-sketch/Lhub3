class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def recur(i,n):
            if i==n:
                res.append(nums[:])
                return
            for j in range(i,n):
                nums[i],nums[j]=nums[j],nums[i]
                recur(i+1,n)
                nums[i],nums[j]=nums[j],nums[i]
                
                
                
        recur(0,len(nums))
        return res