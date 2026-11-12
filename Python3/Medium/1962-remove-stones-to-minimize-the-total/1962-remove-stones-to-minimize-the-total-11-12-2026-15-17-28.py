class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:

        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            currPile = -heapq.heappop(piles)

            currPile = (currPile + 1) // 2
            heapq.heappush(piles, -currPile)

        count = 0
        for pile in piles:
            count += -pile

        return count
