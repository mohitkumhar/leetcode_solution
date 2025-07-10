class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        n = len(piles) // 3 

        for i in range(n):
            piles.pop()
            total += piles.pop()
            piles.pop(0)

        return total
