class RangeAddPointQuery:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        self.tree[self.n:] = arr

    def add(self, l, r, delta):

        l += self.n
        r += self.n

        while l < r:

            if l % 2:
                self.tree[l] += delta
                l += 1

            if r % 2:
                r -= 1
                self.tree[r] += delta

            l //= 2
            r //= 2

    def get(self, i):

        p = i + self.n
        result = 0

        while p:
            result += self.tree[p]
            p //= 2

        return result