class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def solve(i, j, currStrLen):
            if i >= len(s) or j >= len(t):
                if currStrLen == len(t):
                    return 1
                return 0

            # skip
            skip = solve(i + 1, j, currStrLen)

            # take
            take = 0
            if s[i] == t[j]:
                take = solve(i + 1, j + 1, currStrLen + 1)

            return skip + take

        return solve(0, 0, 0)
