class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        if k==n:return len(set(arr))==1
        total=sum(arr)
        if total%k!=0:
            return False
        target=total//k
        if max(arr)>target:
            return False
        dp={0:0}
        for mask in range(1<<n):
            if mask not in dp:continue
            for i,num in enumerate(arr):
                if not (mask & 1<<i) and dp[mask]+num<=target:
                    dp[mask|1<<i]=(dp[mask]+num)%target
        if (1<<n)-1 in dp and dp[(1<<n)-1]==0:
            return True
        return False