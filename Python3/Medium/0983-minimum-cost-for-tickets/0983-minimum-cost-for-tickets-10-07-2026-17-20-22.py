class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:

        def solve(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            # 1 days
            cost_1 = costs[0] + solve(i + 1)

            # 7 days
            maxDays = days[i] + 7
            j = i

            while j < n and days[j] < maxDays:
                j += 1
            cost_7 = costs[1] + solve(j)

            # 30 days
            maxDays = days[i] + 30
            j = i

            while j < n and days[j] < maxDays:
                j += 1
            cost_30 = costs[2] + solve(j)

            memo[i] = min(cost_1, cost_7, cost_30)

            return memo[i]

        n = len(days)
        memo = [-1] * (n + 1)

        return solve(0)
