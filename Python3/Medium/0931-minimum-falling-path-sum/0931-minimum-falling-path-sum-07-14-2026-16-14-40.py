class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        min_path = float("inf")

        memo = [[-101 for _ in range(n)] for _ in range(m)]

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, m):
            for j in range(n):
                up = matrix[i][j] + dp[i - 1][j]

                up_right = float("inf")
                if j < (n - 1):
                    up_right = matrix[i][j] + dp[i - 1][j + 1]

                up_left = float("inf")
                if j > 0:
                    up_left = matrix[i][j] + dp[i - 1][j - 1]

                dp[i][j] = min(up, up_right, up_left)

        return min(dp[m - 1])
