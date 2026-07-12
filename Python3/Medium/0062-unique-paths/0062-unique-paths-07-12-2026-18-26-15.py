class Solution:
    def solve(self, i: int, j: int, m: int, n: int, memo: List[List[int]]) -> int:
        if i >= m or j >= n:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        if memo[i][j] != -1:
            return memo[i][j]

        down = self.solve(i + 1, j, m, n, memo)
        right = self.solve(i, j + 1, m, n, memo)

        memo[i][j] = down + right
        return memo[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.solve(0, 0, m, n, memo)
