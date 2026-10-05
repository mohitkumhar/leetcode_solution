class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # def solve(i, j):
        #     if i >= m or j >= n:
        #         return 0

        #     if memo[i][j] != -1:
        #         return memo[i][j]

        #     take = 0
        #     if text1[i] == text2[j]:
        #         take = 1 + solve(i + 1, j + 1)

        #     skip_i = solve(i + 1, j)
        #     skip_j = solve(i, j + 1)

        #     memo[i][j] = max(take, skip_i, skip_j)
        #     return memo[i][j]

        # m = len(text1)
        # n = len(text2)

        # memo = [[-1 for _ in range(n)] for _ in range(m)]

        # return solve(0, 0)

        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)
        return dp[m][n]
