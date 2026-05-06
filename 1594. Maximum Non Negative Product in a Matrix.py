class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10** 9 + 7

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = (grid[0][0], grid[0][0])

        for i in range(1, m):
            dp[i][0] = (grid[i][0] * dp[i-1][0][0], grid[i][0] * dp[i-1][0][1])
        for j in range(1, n):
            dp[0][j] = (grid[0][j] * dp[0][j-1][0], grid[0][j] * dp[0][j-1][1])


        for i in range(1, m):
            for j in range(1, n):

                top_min = grid[i][j] * dp[i - 1][j][0]
                top_max = grid[i][j] * dp[i - 1][j][1]

                left_min = grid[i][j] * dp[i][j - 1][0]
                left_max = grid[i][j] * dp[i][j - 1][1]

                max_val = max(top_min, top_max, left_max, left_min)
                min_val = min(top_min, top_max, left_max, left_min)

                dp[i][j] = (min_val, max_val)

        return dp[m-1][n-1][1] % MOD if dp[m-1][n-1][1] >= 0 else -1
