class Solution:
    def clearStars(self, s: str) -> str:

        heap = []
        s = list(s)

        for i in range(len(s)):

            if s[i] == "*":
                char, idx = heapq.heappop(heap)
                s[-idx] = "*"
                continue

            heapq.heappush(heap, ((s[i], -i)))

        ans = ""
        for char in s:
            if char != "*":
                ans += char

        return ans
