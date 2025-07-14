class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)

        cost.sort()
        min_cost = 0
        while cost and (len(cost) > 3 or len(cost) % 3 == 0):
            print(len(cost) % 3)
            min_cost += (cost.pop() + cost.pop())
            cost.pop()

        if cost:
            min_cost += sum(cost)

        return min_cost
