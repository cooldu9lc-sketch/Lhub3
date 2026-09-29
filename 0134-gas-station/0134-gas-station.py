class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total_gas=0
        total_cost=0
        n=len(gas)

        start_idx=curr=0
        for i,(g,c) in enumerate(zip(gas,cost)):
            total_gas+=g
            total_cost+=c
            curr+=g-c
            if curr<0:
                curr=0
                start_idx=(i+1)%n



        return start_idx if total_gas>=total_cost else -1