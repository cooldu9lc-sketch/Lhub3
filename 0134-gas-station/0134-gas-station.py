class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total_gas=0
        total_cost=0

        start_idx=curr=0

        for i in range(n):
            total_cost+=cost[i]
            total_gas += gas[i] 
            curr= curr+gas[i]-cost[i] ##TO GET TO INDEX i
            if curr<0:
                curr=0
                start_idx = (i+1)
        return -1 if total_gas<total_cost else start_idx