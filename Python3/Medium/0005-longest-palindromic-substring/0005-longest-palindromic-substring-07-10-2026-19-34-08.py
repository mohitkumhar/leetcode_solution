class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check(string: str) -> bool:
            return string == string[::-1]

        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i, n):
                if check(s[i: j + 1]):
                    if (j - i + 1) > len(ans):
                        ans = s[i: j+1]

        return ans
