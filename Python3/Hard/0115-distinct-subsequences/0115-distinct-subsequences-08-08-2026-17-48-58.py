class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        def solve(i, j, count):
            if i >= len(s) or j >= len(t):
                if count == len(t):
                    memo[i][j] = 1
                    return 1
                memo[i][j] = 0
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            take = 0
            # take
            if s[i] == t[j]:
                take = solve(i + 1, j + 1, count + 1)

            # skip
            skip = solve(i + 1, j, count)

            memo[i][j] = take + skip
            return memo[i][j]

        return solve(0, 0, 0)
