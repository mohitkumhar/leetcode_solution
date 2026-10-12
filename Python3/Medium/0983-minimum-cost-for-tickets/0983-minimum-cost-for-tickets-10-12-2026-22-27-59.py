class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:

        def solve(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            # for 1 day trip
            day_1 = costs[0] + solve(i + 1)

            # for 7 day trip
            maxDays = days[i] + 7
            j = i
            while j < n and days[j] < maxDays:
                j += 1
            day_7 = costs[1] + solve(j)

            # for 30 day trip
            maxDays = days[i] + 30
            j = i

            while j < n and days[j] < maxDays:
                j += 1
            day_30 = costs[2] + solve(j)

            memo[i] = min(day_1, day_7, day_30)

            return memo[i]

        n = len(days)
        memo = [-1 for _ in range(n + 1)]

        return solve(0)
