class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)

        dp = [[0 for _ in range(n + 2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for time in range(n, 0, -1):
                take = time * satisfaction[i] + dp[i + 1][time + 1]
                skip = dp[i + 1][time]

                dp[i][time] = max(take, skip)

        return dp[i][time]
