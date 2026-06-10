from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap=[]
        size = k
        for num in nums:
            if len(heap)<size:
               heappush(heap, num)
            else:
                heappushpop(heap, num)
        return heap[0]
            

        