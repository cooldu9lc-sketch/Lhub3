class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        i=0
        j=len(height)-1
        while i<=j:
            w=(j-i)
            h=min(height[i],height[j])
            res=max(res,w*h)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res


        """
        i,j=0,len(height)-1
        total,maxTotal=0,0

        while i<j:
            x = min(height[i],height[j])
            total=x*(j-i)
            maxTotal = max(total,maxTotal)
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                i+=1
                j-=1
        
        return maxTotal"""