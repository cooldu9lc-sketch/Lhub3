class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        d = lambda i : points[i][0]**2 + points[i][1]**2
            
        def quickselect(l,r):
            pivot_element=random.randint(l,r)
            points[pivot_element],points[r]=points[r],points[pivot_element]
            pivot=d(r)
            pi=l
            for i in range(l,r):
                if d(i)<=pivot:
                    points[pi],points[i]=points[i],points[pi]
                    pi+=1
            points[pi],points[r]=points[r],points[pi]
            return pi
            
        n=len(points)
        l,r=0,n-1
        k=k-1  ###IMPORTANT STEP
        while l<r:
            pivot_index=quickselect(l,r)
            if pivot_index==k:
                return points[:k+1]
            elif pivot_index<k:
                l=pivot_index+1
            else:
                r=pivot_index-1
        return points[:l+1]