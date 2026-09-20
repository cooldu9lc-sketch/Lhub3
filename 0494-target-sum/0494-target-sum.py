
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        totalSum = sum(nums)
        

        required = (target + totalSum)//2
     
        if (target + totalSum) %2==1 or abs(target)>totalSum: return 0

        dp =[0] * (required+1)
        dp[0]=1

        for num in nums:
            for w in range(required,num-1,-1):
                dp[w]+= dp[w-num]
        return dp[-1]