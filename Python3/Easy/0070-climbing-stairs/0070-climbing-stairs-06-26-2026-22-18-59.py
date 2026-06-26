class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1] * (n + 1)
        def solve(curr_stair):
            if curr_stair <= 2:
                return curr_stair
            if memo[curr_stair] != -1:
                return memo[curr_stair]

            memo[curr_stair] = solve(curr_stair - 2) + solve(curr_stair - 1)
            return memo[curr_stair]

        return solve(n)
