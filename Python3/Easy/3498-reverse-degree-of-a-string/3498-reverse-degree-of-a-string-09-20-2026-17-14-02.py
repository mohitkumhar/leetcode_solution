class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            char = s[i]
            val = ord(char) - ord("a") + 1
            reverseVal = 27 - val

            ans += (i + 1) * reverseVal

        return ans
