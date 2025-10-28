class Solution:
    def __init__(self):
        self.memo = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        min_amount = float("inf")

        for coin in coins:
            res = self.coinChange(coins, amount - coin)
            if res >= 0:
                min_amount = min(min_amount, res + 1)
            self.memo[amount] = -1 if min_amount == float("inf") else min_amount

        return self.memo[amount]
