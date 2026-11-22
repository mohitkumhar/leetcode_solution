class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        def solve(i):
            if i <= 2:
                return i
            if i == 3:
                return 5
            if memo[i] != -1:
                return memo[i]

            memo[i] = (2 * solve(i - 1) + solve(i - 3)) % MOD
            return memo[i]

        memo = [-1] * (n + 1)
        return solve(n)
