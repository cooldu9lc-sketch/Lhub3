class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def ispossible(bloom):
            flowers = bouquets=0
            for day in bloomDay:
                if day >bloom:
                    flowers= 0
                else:
                    bouquets+= (flowers+1)//k
                    flowers = (flowers +1)%k
                  
            return bouquets>=m
        if len(bloomDay) < m*k:
            return -1

        ## EACH element in arr i.e arr[i] represents a single flower
        left,right=1,max(bloomDay)
        while left<right:
            mid = (left+right)//2
            if ispossible(mid):
                right=mid
            else:
                left=mid+1
        return left