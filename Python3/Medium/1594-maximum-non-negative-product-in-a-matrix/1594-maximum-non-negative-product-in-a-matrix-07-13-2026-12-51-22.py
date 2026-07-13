class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = (grid[0][0], grid[0][0])

        print(dp)

        for i in range(1, m):
            dp[i][0] = (grid[i][0] * dp[i - 1][0][0], grid[i][0] * dp[i - 1][0][1])
        for j in range(1, n):
            dp[0][j] = (grid[0][j] * dp[0][j - 1][0], grid[0][j] * dp[0][j - 1][1])

        print(dp)

        for i in range(1, m):
            for j in range(1, n):
                top_max = max(
                    grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1]
                )
                top_min = min(
                    grid[i][j] * dp[i - 1][j][0], grid[i][j] * dp[i - 1][j][1]
                )

                right_max = max(
                    grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1]
                )
                right_min = min(
                    grid[i][j] * dp[i][j - 1][0], grid[i][j] * dp[i][j - 1][1]
                )

                dp[i][j] = (max(top_max, right_max), min(top_min, right_min))

        MOD = 10**9 + 7
        m = dp[m - 1][n - 1][0]

        return m % MOD if m >= 0 else -1
