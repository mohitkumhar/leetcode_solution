class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def solve(i, j):
            if i >= m or j >= n:
                return float("inf")
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if memo[i][j] != -1:
                return memo[i][j]

            down = grid[i][j] + solve(i + 1, j)
            right = grid[i][j] + solve(i, j + 1)

            memo[i][j] = min(down, right)
            return memo[i][j]

        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return solve(0, 0)
