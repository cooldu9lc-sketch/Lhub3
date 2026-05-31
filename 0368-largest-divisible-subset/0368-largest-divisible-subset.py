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

        """ Build the dynamic programming matrix/vector """
        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])

            maxSubsetSize += 1
            dp[i] = maxSubsetSize

        """ Find both the size of largest divisible set and its index """
        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        ret = []

        """ Reconstruct the largest divisible subset """
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]

        return ret[::-1]