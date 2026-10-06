class Solution:
    def numTilings(self, n: int) -> int:

        def solve(n):
            if n == 1 or n == 2:
                return n
            if n == 3:
                return 5

            if memo[n] != -1:
                return memo[n]

            memo[n] = (2 * solve(n - 1) + solve(n - 3)) % MOD
            return memo[n]

        MOD = 10**9 + 7
        memo = [-1] * (n + 1)

        return solve(n)
