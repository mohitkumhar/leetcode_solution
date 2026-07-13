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

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        m, _ = self.solve(0, 0, m, n, grid, memo)
        MOD = 10 ** 9 + 7

        return m % MOD if m >= 0 else -1
