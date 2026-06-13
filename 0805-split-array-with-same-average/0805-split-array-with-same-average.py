class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 1: 
            return False
            
        S = sum(nums)
        if not any((S * k) % n == 0 for k in range(1, n // 2 + 1)):
            return False
            
        # Transform the array so the target average becomes strictly 0
        A = [x * n - S for x in nums]
        
        left, right = A[:n//2], A[n//2:]
        
        # Helper function: Maps each generated sum to a set of subset lengths
        def get_subset_sums_with_lengths(arr):
            sums = {0: {0}}  # sum -> set of lengths
            for x in arr:
                next_sums = {}
                for s, lengths in sums.items():
                    for l in lengths:
                        if s + x not in next_sums:
                            next_sums[s + x] = set()
                        next_sums[s + x].add(l + 1)
                        
                # Merge the newly generated combinations into our main dictionary
                for s, lengths in next_sums.items():
                    if s not in sums:
                        sums[s] = set()
                    sums[s].update(lengths)
            return sums

        left_sums = get_subset_sums_with_lengths(left)
        # Check if a valid non-empty proper subset entirely in the left half sums to 0
        if 0 in left_sums and any(l > 0 for l in left_sums[0]):
            return True
            
        right_sums = get_subset_sums_with_lengths(right)
        # Check if a valid non-empty proper subset entirely in the right half sums to 0
        if 0 in right_sums and any(0 < l < n for l in right_sums[0]):
            return True
            
        # The "Meet" phase: check if any left sum has an exact opposite in the right sum
        for s, left_lengths in left_sums.items():
            if -s in right_sums:
                right_lengths = right_sums[-s]
                # We must ensure we don't pick the ENTIRE array (left_l + right_l == n)
                # nor the EMPTY array (left_l + right_l == 0)
                if any(0 < left_l + right_l < n for left_l in left_lengths for right_l in right_lengths):
                    return True
                    
        return False