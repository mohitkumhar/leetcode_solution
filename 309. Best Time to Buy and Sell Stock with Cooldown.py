class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def solve(i, bought):
            if i >= n:
                return 0

            if memo[i][bought] != -1:
                return memo[i][bought]

            buy = 0
            if not bought:
                buy = solve(i + 1, True) - prices[i]
            buy_skip = solve(i + 1, bought)

            sell = 0
            if bought:
                sell = solve(i + 2, False) + prices[i]
            sell_skip = solve(i + 1, bought)
            
            result = max(buy, buy_skip, sell, sell_skip)

            memo[i][bought] = result
            return result

        ans = solve(0, False)

        return ans
