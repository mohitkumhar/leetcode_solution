class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count < 0:
                heapq.heappush(heap, (count, char))

        prev = None
        ans = []

        while heap:

            maxCharCount, maxChar = heapq.heappop(heap)
            maxCharCount = -maxCharCount

            if prev and -prev[0] >= maxCharCount:
                take = 1
            else:
                take = min(maxCharCount, 2)

            ans.append(maxChar * take)
            maxCharCount -= take

            if prev:
                heapq.heappush(heap, prev)

            if maxCharCount > 0:
                prev = (-maxCharCount, maxChar)
            else:
                prev = None

        result = ""

        for word in ans:
            if word == "":
                return result
            result += word

        return ''.join(result)
