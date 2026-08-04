class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        maxProfit = 0
        buyPrice = float("inf")

        for i in range(n):
            buyPrice = min(buyPrice, prices[i])

            profit = prices[i] - buyPrice

            maxProfit = max(maxProfit, profit)

        return maxProfit
