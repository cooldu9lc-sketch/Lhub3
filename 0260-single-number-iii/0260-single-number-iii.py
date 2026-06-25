class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
           
        # Step 1: Get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        # Step 2: Isolate the rightmost set bit
        # Note: Using xor_all & -xor_all
        rightmost_set_bit = xor_all & -xor_all
        
        # Step 3: Divide into two groups and XOR them
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]