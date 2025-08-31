class Solution:
    def fillCups(self, amount: List[int]) -> int:
        sec = 0
        while max(amount) > 0:
            amount.sort(reverse=True)
            if amount[0] > 0:
                amount[0] -= 1
                amount[1] -= 1
            else:
                amount[1] -= 1
            sec += 1
        return sec