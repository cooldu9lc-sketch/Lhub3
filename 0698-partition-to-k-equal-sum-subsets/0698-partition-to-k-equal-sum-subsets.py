class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        arr.sort(reverse=True)
        target,rem =divmod(sum(arr),k)
        if rem or arr[0]>target:return False
        
        dp={0:0}
        for mask in range(2**n):
            if mask not in dp:continue
            for i,num in enumerate(arr):
                if not (mask & 1<<i) and dp[mask]+num<=target:
                    dp[mask|1<<i]=(dp[mask]+num)%target
 
        return (1<<n)-1 in dp and dp[(1<<n)-1]==0