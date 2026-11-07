class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n = len(s)

        result = 0

        last_a = -1
        last_ab = -1

        i = 0
        j = 0

        while j < n:
            if s[j] == "a":
                last_a = j

            elif s[j] == "b":
                if last_a != -1:
                    last_ab = last_a

            elif s[j] == "c":
                if last_ab != -1:
                    i = max(i, last_ab + 1)

            result += j - i + 1

            j += 1

        return result
