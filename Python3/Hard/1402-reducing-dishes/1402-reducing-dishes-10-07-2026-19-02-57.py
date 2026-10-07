class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:

        def solve(i, time):
            if i >= n:
                return 0

            if memo[i][time] != -1:
                return memo[i][time]

            take = time * satisfaction[i] + solve(i + 1, time + 1)
            skip = solve(i + 1, time)

            memo[i][time] = max(take, skip)

            return memo[i][time]

        satisfaction.sort()
        n = len(satisfaction)

        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        return solve(0, 1)
