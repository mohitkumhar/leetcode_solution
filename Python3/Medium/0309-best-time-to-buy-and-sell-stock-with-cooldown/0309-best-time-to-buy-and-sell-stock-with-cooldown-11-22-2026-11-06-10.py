class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            buyStock = dp[i + 1][1] - prices[i]
            skipBuyStock = dp[i + 1][0]

            sellStock = dp[i + 2][0] + prices[i]
            skipSellStock = dp[i + 1][1]

            dp[i][0] = max(buyStock, skipBuyStock)
            dp[i][1] = max(sellStock, skipSellStock)

        return dp[0][0]
