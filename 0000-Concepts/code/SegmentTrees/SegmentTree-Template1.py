class SegmentTree:
    def __init__(self, arr, combine, identity):
        self.n = len(arr)
        self.combine = combine
        self.identity = identity
        self.tree = [identity] * (2 * self.n)

        self.tree[self.n:] = arr

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = combine(
                self.tree[2*i],
                self.tree[2*i + 1]
            )

    def update(self, i, value):
        p = i + self.n
        self.tree[p] = value

        while p > 1:
            p //= 2

            self.tree[p] = self.combine(
                self.tree[2*p],
                self.tree[2*p + 1]
            )

    def query(self, l, r):
        l += self.n
        r += self.n

        left_result = self.identity
        right_result = self.identity

        while l < r:

            if l % 2:
                left_result = self.combine(
                    left_result,
                    self.tree[l]
                )
                l += 1

            if r % 2:
                r -= 1

                right_result = self.combine(
                    self.tree[r],
                    right_result
                )

            l //= 2
            r //= 2

        return self.combine(
            left_result,
            right_result
        )
        )