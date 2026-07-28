class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        LHP = [0] * n
        LHP[0] = 0
        length_idx = 0

        i = 1

        while i < n:
            if s[i] == s[length_idx]:
                length_idx += 1
                LHP[i] = length_idx
                i += 1

            else:
                if length_idx > 0:
                    length_idx = LHP[length_idx - 1]
                else:
                    LHP[i] = 0
                    i += 1

        return s[0 : LHP[n - 1]]
