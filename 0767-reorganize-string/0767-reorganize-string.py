from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-cnt, char)
                for char, cnt in Counter(s).items()]
        heapify(heap)

        prev = (0, "")
        ans = []

        while heap:
            count, char = heappop(heap)
            ans.append(char)

            count += 1

            # Release previously used character
            if prev[0] < 0:
                heappush(heap, prev)

            # Current character is temporarily blocked
            prev = (count, char)

        return "".join(ans) if len(ans) == len(s) else ""