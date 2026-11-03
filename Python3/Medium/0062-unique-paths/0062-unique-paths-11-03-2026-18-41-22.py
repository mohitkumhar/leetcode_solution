class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            down = solve(i + 1, j)
            right = solve(i, j + 1)

            memo[i][j] = down + right
            return memo[i][j]

        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return solve(0, 0)
