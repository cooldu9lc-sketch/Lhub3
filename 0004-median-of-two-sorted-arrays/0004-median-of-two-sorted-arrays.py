class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left_elements = (m + n + 1) // 2
        
        while low <= high:
            # i is the partition pointer for nums1
            i = (low + high) // 2
            # j is the partition pointer for nums2
            j = total_left_elements - i
            
            # Determine the boundary elements (handle edge cases with infinity)
            A_left_max = nums1[i - 1] if i > 0 else float('-inf')
            A_right_min = nums1[i] if i < m else float('inf')
            
            B_left_max = nums2[j - 1] if j > 0 else float('-inf')
            B_right_min = nums2[j] if j < n else float('inf')
            
            # Check if we found the perfect partition
            if A_left_max <= B_right_min and B_left_max <= A_right_min:
                # If odd total, median is just the max of the left side
                if (m + n) % 2 == 1:
                    return float(max(A_left_max, B_left_max))
                # If even total, median is the average of the middle two
                else:
                    return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min)) / 2.0
                    
            elif A_left_max > B_right_min:
                # We took too many elements from nums1, move left
                high = i - 1
            else:
                # We took too few elements from nums1, move right
                low = i + 1
                
        return 0.0