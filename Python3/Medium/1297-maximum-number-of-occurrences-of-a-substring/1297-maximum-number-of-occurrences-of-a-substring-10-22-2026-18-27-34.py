class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        charFreq = {}
        freq = {}

        i = 0
        j = 0
        n = len(s)

        ans = 0

        while j < n:
            charFreq[s[j]] = charFreq.get(s[j], 0) + 1

            if j - i + 1 > minSize:
                char = s[i]
                charFreq[char] = charFreq.get(char, 0) - 1

                if charFreq[char] == 0:
                    del charFreq[char]

                i += 1

            if minSize <= (j - i + 1) <= maxSize:
                if len(charFreq) <= maxLetters:
                    substring = s[i : j + 1]
                    freq[substring] = freq.get(substring, 0) + 1
                    ans = max(ans, freq[substring])

            j += 1

        return ans
