class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_count = 0
    # Keep shifting right until the prefixes match
        while left != right:
            left >>= 1
            right >>= 1
            shift_count += 1
            
        # Shift the common prefix back to its original position
        return left << shift_count