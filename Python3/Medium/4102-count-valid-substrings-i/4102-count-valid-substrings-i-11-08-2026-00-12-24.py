class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n = len(s)

        i = 0
        j = 0

        result = 0

        while j < n:
            if j >= 2 and s[j - 2] == "a" and s[j - 1] == "b" and s[j] == "c":
                i = j - 1

            result += j - i + 1
            j += 1

        return result
