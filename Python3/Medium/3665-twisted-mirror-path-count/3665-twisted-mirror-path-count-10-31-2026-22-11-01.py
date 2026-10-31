class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        def solve(i, j, cameFrom):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            cf = 1 if cameFrom == "LEFT" else 0
            if memo[i][j][cf] != -1:
                return memo[i][j][cf]

            total = 0

            if grid[i][j] == 0:
                total = (total + solve(i, j + 1, "LEFT")) % MOD
                total = (total + solve(i + 1, j, "UP")) % MOD

            else:
                if cameFrom == "LEFT":
                    total = (total + solve(i + 1, j, "UP")) % MOD

                else:
                    total = (total + solve(i, j + 1, "LEFT")) % MOD

            memo[i][j][cf] = total % MOD
            return memo[i][j][cf]

        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        memo = [[[-1 for _ in range(2)] for _ in range(n + 1)] for _ in range(m + 1)]

        return solve(0, 0, "LEFT")
