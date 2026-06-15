class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        A = intervals
        A = sorted(A,reverse=True) ## ARRAY IS REVERSEDD TO POP
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q: #
                i, j = A.pop()
                if j >= q: ##if j < q , j will be useless for this query and all queries after
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q: ### clean up all the finished intervvals
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]