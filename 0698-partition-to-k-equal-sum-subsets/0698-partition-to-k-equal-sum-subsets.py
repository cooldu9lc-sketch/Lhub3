class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        mask = 0
        
        memo = {}
        
        def backtrack(index, count, curr_sum):
            nonlocal mask
            n = len(arr)
            
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
            
            # If we have already computed the current combination.
            if mask in memo:
                return memo[mask]
            
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[mask] = backtrack(0, count + 1, 0)
                return memo[mask]

            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if ((mask >> j) & 1) == 0:
                    # Include this element in current subset.
                    mask = (mask | (1 << j))

                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    # Backtrack step.
                    mask = (mask ^ (1 << j))

            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            memo[mask] = False
            return memo[mask] 

        return backtrack(0, 0, 0)