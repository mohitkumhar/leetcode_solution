class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0
        curr = s[0]

        for i in range(n):
            if s[i] != curr:
                count += 1

            curr = "0" if curr == "1" else "1"

        return min(count, n - count)
