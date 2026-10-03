class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        def solve(i, j):
            if i >= m or j >= n or j < 0:
                return float("inf")
            if i == (n - 1):
                return matrix[i][j]

            bottomLeft = matrix[i][j] + solve(i + 1, j - 1)
            bottomDown = matrix[i][j] + solve(i + 1, j)
            bottomRight = matrix[i][j] + solve(i + 1, j + 1)

            return min(bottomLeft, bottomDown, bottomRight)

        m = len(matrix)
        n = len(matrix[0])
        result = float("inf")

        for j in range(m):
            result = min(result, solve(0, j))

        return result
