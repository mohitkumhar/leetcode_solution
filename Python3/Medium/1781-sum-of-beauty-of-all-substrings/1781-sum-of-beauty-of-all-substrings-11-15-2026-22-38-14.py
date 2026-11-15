class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            freq = {}
            maxFreq = float("-inf")
            minFreq = float("inf")

            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                maxFreq = max(maxFreq, freq[s[j]])
                minFreq = min(freq.values())

                count += maxFreq - minFreq

        return count
