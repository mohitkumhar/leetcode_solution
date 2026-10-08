class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:

        def solve(i, currProfit, people):
            if i == len(group):
                return 1 if currProfit >= minProfit else 0

            if memo[i][currProfit][people] != -1:
                return memo[i][currProfit][people]

            take = 0
            if (people + group[i]) <= n:
                newProfit = min(minProfit, currProfit + profit[i])
                take = solve(i + 1, newProfit, people + group[i])

            skip = solve(i + 1, currProfit, people) % MOD

            memo[i][currProfit][people] = (take + skip) % MOD

            return memo[i][currProfit][people]

        memo = [
            [[-1 for _ in range(n + 1)] for _ in range(minProfit + 1)]
            for _ in range(len(group))
        ]

        MOD = 10**9 + 7

        return solve(0, 0, 0)
