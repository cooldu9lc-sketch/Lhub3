class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007
        SQ_MATRIX = [[1, 1, 2], [1, 0, 0], [0, 1, 1]]  # Initialize square matrix
        SIZE = 3  # Width/Length of square matrix

        def matrix_product(m1, m2):  
            """Return product of 2 square matrices."""
            nonlocal MOD, SIZE
            # Result matrix `ans` will also be a square matrix with same dimension
            ans = [[0] * SIZE for _ in range(SIZE)]  
            for row in range(SIZE):
                for col in range(SIZE):
                    cur_sum = 0
                    for k in range(SIZE):
                        cur_sum = (cur_sum + m1[row][k] * m2[k][col]) % MOD
                    ans[row][col] = cur_sum
            return ans

        @cache  
        def matrix_expo(n):
            nonlocal SQ_MATRIX
            if n == 1:  # base case
                return SQ_MATRIX
            elif n % 2:  # If `n` is odd
                return matrix_product(matrix_expo(n - 1), SQ_MATRIX)
            else:  # If `n` is even
                return matrix_product(matrix_expo(n // 2), matrix_expo(n // 2))

        if n <= 2:
            return n

        # The answer will be cur[0][0] * f(2) + cur[0][1] * f(1) + cur[0][2] * p(2)
        ans = matrix_expo(n - 2)[0]
        return (ans[0] * 2 + ans[1] * 1 + ans[2] * 1) % MOD