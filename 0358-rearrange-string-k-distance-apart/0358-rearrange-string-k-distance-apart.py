from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        heap = [(-cnt, ch) for ch, cnt in Counter(s).items()]
        heapify(heap)
        cooldown = deque()  # (negative remaining count, character)
        ans = []

        while heap:
            cnt, ch = heappop(heap)
            ans.append(ch)
            cnt += 1  # negative count moves toward 0
            cooldown.append((cnt, ch))

            # A character chosen k positions ago is now eligible.
            if len(cooldown) >= k:
                old_cnt, old_ch = cooldown.popleft()
                if old_cnt < 0:
                    heappush(heap, (old_cnt, old_ch))

        return "".join(ans) if len(ans) == len(s) else ""
