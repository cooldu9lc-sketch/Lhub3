class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])

        r,c=m-1,0
        while r>=0 and c<n:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                c+=1
            else:
                r-=1
        return False