class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        ans = []
        for _ in range(k):
            count, string = heapq.heappop(heap)
            ans.append(string)

        return ans
