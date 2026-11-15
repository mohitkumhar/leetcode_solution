class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i, j):
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break

                i -= 1
                j += 1

            return s[i + 1 : j]

        ans = ""

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(ans):
                ans = odd

            if len(even) > len(ans):
                ans = even

        return ans
