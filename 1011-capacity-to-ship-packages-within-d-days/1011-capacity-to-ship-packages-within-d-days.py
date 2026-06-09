class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ispossible(weight):
            total=0
            time=1
            for w in weights:
                if w+total<=weight:
                    total+=w
                else:
                    total=w
                    time+=1
                    if time>days:
                        return False
            return True
        
        
        left,right=max(weights),sum(weights)
        while left<right:
            mid = (left+right)//2
            if ispossible(mid):
                right=mid
            else:
                left=mid+1
        return left