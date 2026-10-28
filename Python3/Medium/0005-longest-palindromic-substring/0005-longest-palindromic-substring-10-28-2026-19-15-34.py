class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i, n):
                subStr = s[i : j + 1]

                if subStr == subStr[::-1] and len(subStr) > len(ans):
                    ans = subStr

        return ans
