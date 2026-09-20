class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        # important step !
        nums.sort()

        # The container that keep the size of the largest divisible subset that ends with X_i
        # dp[i] corresponds to len(EDS(X_i))
        dp = [0] * (len(nums))
        parent= [-1]*(len(nums))
       

        """ Build the dynamic programming matrix/vector """
        for i, num in enumerate(nums):
            for k in range(0, i):
                if num % nums[k] == 0 and dp[k]+1>dp[i]:
                    dp[i] = dp[k]+1
                    parent[i]=k
        ret=[]
        maxSubsetSize = max(dp)
        idx = dp.index(maxSubsetSize)
        while parent[idx]>-1:
            ret.append(nums[idx])
            idx=parent[idx]
        ret.append(nums[idx])
        return ret[::-1]

