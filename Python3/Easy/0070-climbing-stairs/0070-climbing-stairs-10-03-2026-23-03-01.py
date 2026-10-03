class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(n):
            if n <= 2:
                return n
            if memo[n] != -1:
                return memo[n]

            memo[n] = solve(n - 1) + solve(n - 2)
            return memo[n]

        memo = [-1] * (n + 1)

        return solve(n)
