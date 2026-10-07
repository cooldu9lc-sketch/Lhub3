class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
    
        n=len(nums)
        if n==1:return False
        total=sum(nums)
        avg= total/n
        #dp[len][s]= ith bit is set if dp[s] exists for length i
        dp=[0]*(total+1)
        dp[0]|=1
        for i in range(1,n):
            for s in range(total-nums[i],-1,-1):
                if dp[s]:
                    dp[s+nums[i]]|=(dp[s]<<1)
            dp[nums[i]]|=2


        for lenb in range(1,n):
            if (total *lenb)%n==0:
                sumb= int(avg*lenb)
                if dp[sumb] & 1<<lenb:return True
        return False
