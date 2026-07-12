class Solution:
    def solve(
        self,
        i: int,
        j: int,
        m: int,
        n: int,
        grid: List[List[int]],
        memo: List[List[int]],
    ) -> int:
        if i >= m or j >= n:
            return float("inf")
        elif i == m - 1 and j == n - 1:
            return grid[i][j]
        elif memo[i][j] != -1:
            return memo[i][j]

        down = self.solve(i + 1, j, m, n, grid, memo)
        right = self.solve(i, j + 1, m, n, grid, memo)

        memo[i][j] = min(down, right) + grid[i][j]
        return memo[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(0, 0, m, n, grid, memo)
