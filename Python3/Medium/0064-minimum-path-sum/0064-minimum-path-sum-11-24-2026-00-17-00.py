class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        def solve(i, j):
            if i >= m or j >= n:
                return float("inf")
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if memo[i][j] != -1:
                return memo[i][j]

            right = grid[i][j] + solve(i, j + 1)
            down = grid[i][j] + solve(i + 1, j)

            memo[i][j] = min(right, down)
            return memo[i][j]

        m = len(grid)
        n = len(grid[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return solve(0, 0)
