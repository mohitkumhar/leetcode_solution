class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        s = s + s

        count1 = 0
        count2 = 0
        minOp = float("inf")

        s1 = ""
        s2 = ""

        for i in range(2 * n):
            s1 += "0" if i % 2 == 0 else "1"
            s2 += "0" if i % 2 == 1 else "1"

        i = 0
        j = 0

        while j < (2 * n):

            if s[j] != s1[j]:
                count1 += 1
            if s[j] != s2[j]:
                count2 += 1

            if j - i + 1 > n:
                if s[i] != s1[i]:
                    count1 -= 1
                if s[i] != s2[i]:
                    count2 -= 1
                i += 1

            if (j - i + 1) == n:
                minOp = min(minOp, count1, count2)

            j += 1

        return minOp
