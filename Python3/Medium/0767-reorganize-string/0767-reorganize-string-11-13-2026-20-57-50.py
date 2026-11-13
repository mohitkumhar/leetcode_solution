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

        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))

        ans = ""
        prev = None
        while heap:

            value, char = heapq.heappop(heap)

            value = -value

            value -= 1
            ans += char

            if prev:
                heapq.heappush(heap, prev)

            if value > 0:
                prev = (-value, char)
            else:
                prev = None

        return ans
