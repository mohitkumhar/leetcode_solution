class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i, n):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    if j - i + 1 > len(ans):
                        ans = s[i : j + 1]

        return ans
