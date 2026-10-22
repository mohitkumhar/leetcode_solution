class Solution:
    def maxRepOpt1(self, text: str) -> int:

        freq = {}
        ans = 0

        for char in text:
            freq[char] = freq.get(char, 0) + 1

        i = 0
        j = 0

        for char in freq:
            i = 0
            count = 0

            for j in range(len(text)):
                if text[j] != char:
                    count += 1

                while count > 1:
                    if text[i] != char:
                        count -= 1
                    i += 1

                ans = max(ans, min(j - i + 1, freq[char]))

        return ans
