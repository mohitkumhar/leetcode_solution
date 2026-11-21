class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        def solve(i, j):
            if i >= m or j >= n or j < 0:
                return float("inf")
            if i == (m - 1):
                return matrix[i][j]
            if memo[i][j] != -1:
                return memo[i][j]

            bottomLeft = float("inf")
            bottomDown = float("inf")
            bottomRight = float("inf")

            if i < m - 1 and j > 0:
                bottomLeft = matrix[i][j] + solve(i + 1, j - 1)
            if i < m - 1:
                bottomDown = matrix[i][j] + solve(i + 1, j)
            if i < m - 1 and j < n - 1:
                bottomRight = matrix[i][j] + solve(i + 1, j + 1)

            memo[i][j] = min(bottomLeft, bottomDown, bottomRight)
            return memo[i][j]

        m = len(matrix)
        n = len(matrix[0])

        memo = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        result = float("inf")

        for j in range(n):
            result = min(result, solve(0, j))

        return result
