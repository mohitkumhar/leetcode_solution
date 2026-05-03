class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def solve(i, bought):
            if i >= n:
                return 0
            if memo[i][bought] != -1:
                return memo[i][bought]

            buy_stock = 0
            if not bought:
                buy_stock = -prices[i] + solve(i + 1, True)
            buy_stock_skip = solve(i + 1, bought)

            sell_stock = 0
            if bought:
                sell_stock = (prices[i] + solve(i + 1, False)) - fee
            sell_stock_skip = solve(i + 1, bought)

            result = max(buy_stock, buy_stock_skip, sell_stock, sell_stock_skip)
            memo[i][bought] = result

            return result

        ans = solve(0, False)

        return ans
