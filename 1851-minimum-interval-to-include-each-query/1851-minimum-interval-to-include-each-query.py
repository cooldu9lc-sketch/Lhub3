class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        ans = {}
        i=0

        for q in sorted(queries):
            # Add intervals that have started
            while i<len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                if r >= q:
                    heapq.heappush(heap, (r-l+1, r))
                i+=1

            # Lazily remove expired intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            ans[q] = heap[0][0] if heap else -1

        return [ans[q] for q in queries]