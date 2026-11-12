class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            firstHeavyStone = -heapq.heappop(stones)
            secondHeavyStone = -heapq.heappop(stones)

            if firstHeavyStone == secondHeavyStone:
                continue

            else:
                firstHeavyStone -= secondHeavyStone
                heapq.heappush(stones, -firstHeavyStone)

        if stones:
            return -heapq.heappop(stones)
        return 0
