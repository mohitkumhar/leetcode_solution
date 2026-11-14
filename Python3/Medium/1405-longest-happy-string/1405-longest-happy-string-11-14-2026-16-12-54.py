class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        prev = None
        ans = []

        while heap:

            currCharCount, currChar = heapq.heappop(heap)
            currCharCount = -currCharCount

            if prev and -prev[0] >= currCharCount:
                take = 1
            else:
                take = min(currCharCount, 2)

            currCharCount -= take
            ans.append(currChar * take)

            if prev:
                heapq.heappush(heap, prev)

            if currCharCount > 0:
                prev = (-currCharCount, currChar)
            else:
                prev = None

        return "".join(ans)
