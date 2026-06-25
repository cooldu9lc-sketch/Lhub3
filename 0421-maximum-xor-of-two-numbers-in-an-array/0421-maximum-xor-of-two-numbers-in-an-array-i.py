class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        L=len(bin(max(nums))) - 2
        mask=ans=0
        for i in range(L-1,-1,-1):
            mask|=1<<i ###all ones
            prefixes={mask & num for num in nums}
            required=ans|1<<i
            ## we need to find two numbers p1 and p2 in prefixes such that p1^p2=required
            ## meaning p1^required = p2
            
            if any(required^prefix in prefixes for prefix in prefixes):
                ans=required
           
        return ans