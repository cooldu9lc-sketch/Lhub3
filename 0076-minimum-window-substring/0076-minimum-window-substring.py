from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)

        left = 0
        best_start = 0
        best_len = float("inf")

        for right, char in enumerate(s):

            # Add s[right] to the window
            if need[char] > 0:
                missing -= 1

            need[char] -= 1

            # Window contains everything required by t
            while missing == 0:

                # Record current valid window
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                # Remove s[left] from window
                left_char = s[left]
                need[left_char] += 1

                # We removed a required character,
                # so the window becomes invalid
                if need[left_char] > 0:
                    missing += 1

                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]