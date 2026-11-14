class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        freq = sorted(freq.keys(), key=lambda w: (-freq[w], w))

        return freq[:k]
