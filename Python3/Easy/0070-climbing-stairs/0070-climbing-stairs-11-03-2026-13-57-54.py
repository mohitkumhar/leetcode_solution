class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(x):
            if x <= 2:
                return x

            if memo[x] != -1:
                return memo[x]

            total = 0
            total += solve(x - 1)
            total += solve(x - 2)

            memo[x] = total
            return memo[x]

        memo = [-1] * (n + 1)
        return solve(n)
