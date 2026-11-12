class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        queue = []

        for pile in piles:
            heapq.heappush(queue, -pile)

        for _ in range(k):

            currPile = -heapq.heappop(queue)
            currPile = (currPile + 1) // 2

            heapq.heappush(queue, -currPile)

        ans = 0
        for val in queue:
            ans += -val

        return ans
