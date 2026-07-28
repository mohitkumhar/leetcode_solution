class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        mid = n // 2

        s[0:mid] = sorted(s[0:mid])

        i = 0
        j = n - 1

        while i < j:
            s[j] = s[i]

            i += 1
            j -= 1

        return "".join(s)
