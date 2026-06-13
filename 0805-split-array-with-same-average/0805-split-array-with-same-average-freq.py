class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
    
        n = len(nums)
        if n <= 1: 
            return False
            
        S = sum(nums)
        if not any((S * k) % n == 0 for k in range(1, n // 2 + 1)):
            return False
            
        # Transform the array so the target average becomes strictly 0
        A = [x * n - S for x in nums]
        
        # Split the array strictly in half
        left, right = A[:n//2], A[n//2:]
        
        # Helper function to generate all subset sums (excluding the empty subset)
        def get_subset_sums(arr):
            sums = {arr[0]}
            for x in arr[1:]:
                # Add current element to all previously found sums
                sums |= {x}| {v + x for v in sums} 
            #sums.remove(0) # Remove the empty subset
            return sums

        left_sums = get_subset_sums(left)
        if 0 in left_sums: 
            return True
            
        right_sums = get_subset_sums(right)
        
        # CRITICAL: We cannot pick the entire array! 
        # The sum of the full transformed array is exactly 0.
        # If we take the full 'left' and full 'right', they will sum to 0 and give a false positive.
        # We prevent this by simply removing the full sum of the right side from our sets.
        s_right = sum(right)
        right_sums.discard(s_right)
        
        if 0 in right_sums: 
            return True
            
        # The "Meet" phase: check if any left sum has an exact opposite in the right sum
        for x in left_sums:
            if -x in right_sums:
                return True
                
        return False