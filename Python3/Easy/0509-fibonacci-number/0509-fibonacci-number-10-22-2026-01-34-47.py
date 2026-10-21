class Solution:
    def fib(self, n: int) -> int:
        def solve(n):
            if n <= 1:
                return n

            if memo[n] != -1:
                return memo[n]

            memo[n] = solve(n - 2) + solve(n - 1)
            return memo[n]

        memo = [-1] * (n + 1)
        return solve(n)
