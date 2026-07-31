class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for char in word:
            freq[ord(char) - 97] += 1

        freq.sort(reverse=True)

        ans = 0
        for i in range(26):
            char = freq[i]

            press = i // 8 + 1

            ans += char * press

        return ans