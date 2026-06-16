class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        maxFreq = max(freq.values())

        countMax = sum(
            1 for f in freq.values()
            if f == maxFreq
        )

        return max(
            len(tasks),
            (maxFreq - 1) * (n + 1) + countMax
        )