class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyPrice = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            buyPrice = min(buyPrice, prices[i])

            currProfit = prices[i] - buyPrice

            maxProfit = max(maxProfit, currProfit)
        return maxProfit
