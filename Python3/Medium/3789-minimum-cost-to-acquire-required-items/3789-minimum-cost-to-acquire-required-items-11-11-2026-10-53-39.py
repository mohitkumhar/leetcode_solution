class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        ans = 0

        # while both > 0
        costForBoth = min(costBoth, cost1 + cost2)
        both = min(need1, need2)

        ans += costForBoth * both

        need1 -= both
        need2 -= both

        ans += need1 * min(costForBoth, cost1)
        ans += need2 * min(costForBoth, cost2)

        return ans
