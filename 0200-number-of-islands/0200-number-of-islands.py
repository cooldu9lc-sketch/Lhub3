from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        # Union by rank / size
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        self.rank[px] += self.rank[py]

        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        uf = UnionFind(rows * cols)

        # Initially every land cell is its own island
        islands = sum(
            grid[r][c] == "1"
            for r in range(rows)
            for c in range(cols)
        )

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "0":
                    continue

                index = r * cols + c

                # Only check right and down.
                # Left and up would duplicate unions.

                if r + 1 < rows and grid[r + 1][c] == "1":
                    neighbor = (r + 1) * cols + c

                    if uf.union(index, neighbor):
                        islands -= 1

                if c + 1 < cols and grid[r][c + 1] == "1":
                    neighbor = r * cols + (c + 1)

                    if uf.union(index, neighbor):
                        islands -= 1

        return islands