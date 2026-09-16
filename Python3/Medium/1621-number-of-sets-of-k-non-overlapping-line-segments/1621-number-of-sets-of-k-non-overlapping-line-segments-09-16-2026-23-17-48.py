class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for K in range(1, k + 1):

            prevRowSum = [0] * (n + 1)
            for x in range(n - 1, -1, -1):
                prevRowSum[x] = (prevRowSum[x + 1] + dp[x][K - 1]) % MOD

            for i in range(n - 1, -1, -1):
                skip = dp[i + 1][K] % MOD
                take = prevRowSum[i + 1] % MOD

                dp[i][K] = (skip + take) % MOD

        return dp[0][k]
