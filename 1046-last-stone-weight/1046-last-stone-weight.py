class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap =[ ]
        for num in stones:
            heapq.heappush(heap,-num)

        while len(heap)>1:
            y,x= -heappop(heap),-heappop(heap)
            if x==y:continue
            heappush(heap,x-y)

        return -heap[0] if heap else 0