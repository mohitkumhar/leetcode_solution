class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i, n):
                substr = s[i : j + 1]
                if substr == substr[::-1] and j - i + 1 > len(ans):
                    ans = s[i : j + 1]

        return ans
