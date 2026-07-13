class Solution:
    def solve(
        self,
        i: int,
        j: int,
        m: int,
        n: int,
        grid: List[List[int]],
        memo: List[List[int]],
    ) -> tuple(int, int):
        if i == (m - 1) and j == (n - 1):
            return (grid[i][j], grid[i][j])

        if memo[i][j] != -1:
            return memo[i][j]

        max_val = float("-inf")
        min_val = float("inf")

        if (i + 1) < m:
            down_max, down_min = self.solve(i + 1, j, m, n, grid, memo)
            max_val = max(max_val, down_max * grid[i][j], down_min * grid[i][j])
            min_val = min(min_val, down_min * grid[i][j], down_max * grid[i][j])

        if (j + 1) < n:
            right_max, right_min = self.solve(i, j + 1, m, n, grid, memo)
            max_val = max(max_val, right_max * grid[i][j], right_min * grid[i][j])
            min_val = min(min_val, right_min * grid[i][j], right_max * grid[i][j])

        memo[i][j] = (max_val, min_val)
        return memo[i][j]

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
