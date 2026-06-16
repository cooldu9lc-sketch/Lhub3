class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        cooldown = deque()

        ans = []

        while heap:

            cnt, ch = heapq.heappop(heap)

            ans.append(ch)

            cnt += 1          # used once

            cooldown.append((cnt, ch))

            if len(cooldown) >= k:
                old_cnt, old_ch = cooldown.popleft()

                if old_cnt < 0:
                    heapq.heappush(heap, (old_cnt, old_ch))

        return "".join(ans) if len(ans) == len(s) else ""