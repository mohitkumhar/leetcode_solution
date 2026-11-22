class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        def solve(i, bought):
            if i >= n:
                return 0

            if memo[i][bought] != -1:
                return memo[i][bought]

            buyStock = 0
            if not bought:
                buyStock = solve(i + 1, True) - prices[i]
            skipBuyStock = solve(i + 1, bought)

            sellStock = 0
            if bought:
                sellStock = prices[i] + solve(i + 2, False)
            skipSellStock = solve(i + 1, bought)

            memo[i][bought] = max(buyStock, skipBuyStock, sellStock, skipSellStock)

            return memo[i][bought]

        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        return solve(0, False)
