class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        def solve(i, j):
            if i >= m or j >= n or j < 0:
                return float("inf")
            if i == (n - 1):
                return matrix[i][j]

            if memo[i][j] != -1:
                return memo[i][j]

            bottomLeft = matrix[i][j] + solve(i + 1, j - 1)
            bottomDown = matrix[i][j] + solve(i + 1, j)
            bottomRight = matrix[i][j] + solve(i + 1, j + 1)

            memo[i][j] = min(bottomLeft, bottomDown, bottomRight)
            return memo[i][j]

        m = len(matrix)
        n = len(matrix[0])
        result = float("inf")

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            result = min(result, solve(0, j))

        return result
