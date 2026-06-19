class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dfs(i, j):

            if j == len(p):
                return i == len(s)

            if i == len(s):
                return all(ch == '*' for ch in p[j:])

            if p[j] == '*':
                return (
                    dfs(i, j + 1) or
                    dfs(i + 1, j)
                )

            if p[j] == '?' or s[i] == p[j]:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)