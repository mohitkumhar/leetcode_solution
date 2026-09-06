class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        def solve(i, j, currStrLen):
            if i >= len(s) or j >= len(t):
                if currStrLen == len(t):
                    memo[i][j] = 1
                    return 1
                memo[i][j] = 0
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            # skip
            skip = solve(i + 1, j, currStrLen)

            # take
            take = 0
            if s[i] == t[j]:
                take = solve(i + 1, j + 1, currStrLen + 1)

            memo[i][j] = skip + take

            return memo[i][j]

        return solve(0, 0, 0)
