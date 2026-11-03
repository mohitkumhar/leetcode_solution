class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        def solve(i):
            if i == n:
                return True
            if memo[i] != -1:
                return memo[i]

            for end in range(i, n):
                if s[i : end + 1] in wordDict and solve(end + 1):
                    memo[i] = True
                    return memo[i]

            memo[i] = False
            return False

        n = len(s)
        memo = [-1] * (n + 1)

        return solve(0)
