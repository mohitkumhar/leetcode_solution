class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)

        i = 0
        j = n - 1

        while i <= j:
            if s[i] == s[j]:
                return i
            i += 1
            j -= 1

        return -1
