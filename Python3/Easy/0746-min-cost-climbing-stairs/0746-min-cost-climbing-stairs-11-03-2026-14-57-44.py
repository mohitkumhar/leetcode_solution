class Solution:
    def minCostClimbingStairs(self, costs: list[int]) -> int:

        def solve(stairs):
            if stairs <= 1:
                return 0
            if stairs == 2:
                return min(costs[0], costs[1])

            if memo[stairs] != -1:
                return memo[stairs]

            memo[stairs] = min(
                solve(stairs - 1) + costs[stairs - 1],
                solve(stairs - 2) + costs[stairs - 2],
            )

            return memo[stairs]

        stairs = len(costs)
        memo = [-1] * (stairs + 1)

        return solve(stairs)
