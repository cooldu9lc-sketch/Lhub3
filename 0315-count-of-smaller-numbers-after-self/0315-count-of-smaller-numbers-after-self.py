class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr,left,right):
            if left<right:
                mid=(left+right)//2
                mergeSort(arr,left,mid)
                mergeSort(arr,mid+1,right)
                merge(arr,left,right,mid)
       
        def merge(arr,left,right,mid):
            i=left
            j=mid+1
            temp=[]
            while i<=mid and j<=right:
                if arr[i][0]<=arr[j][0]:
                    res[arr[i][1]]+=j-mid-1
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1
            while i<=mid:
                res[arr[i][1]]+=j-mid-1
                temp.append(arr[i])
                i+=1
            while j<=right:
                temp.append(arr[j])
                j+=1
            for x in range(left,right+1):
                arr[x]=temp[x-left]


        arr=[(v,i) for i,v in enumerate(nums)]
        n=len(nums)
        res=[0]*n
        mergeSort(arr,0,n-1)
        return res