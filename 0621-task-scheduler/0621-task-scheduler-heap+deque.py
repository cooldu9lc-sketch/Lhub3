from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap = [-v for v in freq.values()]
        heapq.heapify(heap)

        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(heap, cnt)

        return time