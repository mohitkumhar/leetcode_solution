class Solution:
    def minCostClimbingStairs(self, costs: list[int]) -> int:

        stairs = len(costs)

        dp = [0] * (stairs + 1)
        dp[2] = min(costs[0], costs[1])

        for i in range(3, stairs + 1):
            dp[i] = min(dp[i - 1] + costs[i - 1], dp[i - 2] + costs[i - 2])

        return dp[stairs]
