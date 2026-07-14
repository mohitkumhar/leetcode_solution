class Solution:
    def solve(self, i: int, j: int, matrix: List[List[int]], memo: List[List[int]]):
        if i >= len(matrix) or j >= len(matrix[0]) or j < 0:
            return float("inf")
        elif i == (len(matrix) - 1):
            return matrix[i][j]
        elif memo[i][j] != -101:
            return memo[i][j]

        bottom_left = matrix[i][j] + self.solve(i + 1, j - 1, matrix, memo)
        bottom_down = matrix[i][j] + self.solve(i + 1, j, matrix, memo)
        bottom_right = matrix[i][j] + self.solve(i + 1, j + 1, matrix, memo)

        memo[i][j] = min(bottom_left, bottom_down, bottom_right)
        return memo[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        min_path = float("inf")

        memo = [[-101 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            min_path = min(min_path, self.solve(0, j, matrix, memo))

        return min_path
