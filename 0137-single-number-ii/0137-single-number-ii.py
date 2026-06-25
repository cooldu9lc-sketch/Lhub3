class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Loner. 
        loner = 0
        
        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0
            
            # For this bit, iterate over all integers
            for num in nums:
                
                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1
            
            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        if loner & (1<<31):
            return loner - (1<<32)
        return loner
        # Do not mistaken sign bit for MSB.
       
        return ~( loner ^ 0xFFFFFFFF)
        
      