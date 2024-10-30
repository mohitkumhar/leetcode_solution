class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        freq = {}
        max_freq = 0
        count = 0 
        s = list(s)

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])

            if (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            count = max(count, end - start + 1)

        return count
