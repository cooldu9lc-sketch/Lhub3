import random
class Solution:

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist_sq(p: list[int]) -> int:
            return p[0] * p[0] + p[1] * p[1]

        target_idx = k - 1
        left, right = 0, len(points) - 1

        while left <= right:
            pivot_dist = dist_sq(points[random.randint(left, right)])
            lt, i, gt = left, left, right

            while i <= gt:
                d = dist_sq(points[i])
                if d < pivot_dist:
                    points[lt], points[i] = points[i], points[lt]
                    lt += 1
                    i += 1
                elif d > pivot_dist:
                    points[gt], points[i] = points[i], points[gt]
                    gt -= 1
                else:
                    i += 1

            if lt <= target_idx <= gt:
                break
            elif target_idx < lt:
                right = lt - 1
            else:
                left = gt + 1

        return points[:k]