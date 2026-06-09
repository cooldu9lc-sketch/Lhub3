class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def ispossible(num):
            count = 0 
            for val in range(1,m+1):
                count += min(num//val,n)
            return count>=k
      
        ## EACH element in arr i.e arr[i] represents a single flower
        left,right=1,m*n
        while left<right:
            mid = (left+right)//2
            if ispossible(mid):
                right=mid
            else:
                left=mid+1
        return left
