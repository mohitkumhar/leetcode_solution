class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        def solve(currMoney):
            if currMoney == 0:
                return 0
            if currMoney < 0:
                return float("inf")
            if memo[currMoney] != -1:
                return memo[currMoney]

            minimumCoin = float("inf")

            for coin in coins:
                take = 1 + solve(currMoney - coin)
                minimumCoin = min(minimumCoin, take)

            memo[currMoney] = minimumCoin
            return memo[currMoney]

        memo = [-1] * (amount + 1)
        ans = solve(amount)

        return ans if ans != float("inf") else -1
