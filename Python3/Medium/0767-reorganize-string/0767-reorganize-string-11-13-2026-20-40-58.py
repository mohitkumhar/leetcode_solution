class Solution:
    def reorganizeString(self, s: str) -> str:

        n = len(s)
        if n == 1:
            return s

        maxFreq = (n + 1) // 2

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] > maxFreq:
                return ""

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        ans = ""

        prev = None

        while heap:
            values, char = heapq.heappop(heap)
            values = -values

            ans += char
            values -= 1

            if prev:
                heapq.heappush(heap, prev)

            if values > 0:
                prev = (-values, char)
            else:
                prev = None

        return ans
