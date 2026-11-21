class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(i):
            if i > n:
                return 0
            if i == n:
                memo[i] = 1
                return memo[i]
            if memo[i] != -1:
                return memo[i]

            jump1Step = solve(i + 1)
            jump2Step = solve(i + 2)

            memo[i] = jump1Step + jump2Step
            return memo[i]

        memo = [-1 for _ in range(n + 1)]
        return solve(0)
