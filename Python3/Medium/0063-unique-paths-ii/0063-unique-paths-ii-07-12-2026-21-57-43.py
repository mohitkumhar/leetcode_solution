class Solution:
    def solve(self, i: int, j: int, m: int, n: int, grid: List[List[int]], memo: List[List[int]]):
        if i >= m or j >= n:
            return 0
        if grid[i][j] == 1:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        if memo[i][j] != -1:
            return memo[i][j]

        down = self.solve(i + 1, j, m, n, grid, memo)
        right = self.solve(i, j + 1, m, n, grid, memo)

        memo[i][j] = down + right
        return memo[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solve(0, 0, m, n, obstacleGrid, memo)
