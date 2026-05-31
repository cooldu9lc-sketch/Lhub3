class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n=len(nums)
        dp=[1]*n
        maxlen=1
        parent={}
        res=[]
        for j in range(len(nums)):
            for i in range(j-1,-1,-1):
                if nums[j]%nums[i]==0 and dp[i]+1>dp[j]:
                    dp[j]=dp[i]+1
                    maxlen=max(maxlen,dp[j])
                    parent[j]=i
        for i in range(n-1,-1,-1):
            if dp[i]==maxlen:
                res.append(nums[i])
                break
        maxlen-=1
        curr=i
        while maxlen:
            curr=parent[curr]
            res.append(nums[curr])
            maxlen-=1
        return res[::-1]