class Solution:
    def minimumCost(self, costs: list[int]) -> int:
        costs.sort(reverse=True)

        currCost = 0
        count = 1

        for cost in costs:
            if count == 3:
                count = 1
                continue
            currCost += cost
            count += 1

        return currCost
