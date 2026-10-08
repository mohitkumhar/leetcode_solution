class Solution:
    def numWays(self, words: list[str], target: str) -> int:

        def solve(i, j):
            if i >= len(target):
                return 1
            if j >= len(words[0]):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            skip = solve(i, j + 1) % MOD
            take = (freq[ord(target[i]) - ord("a")][j] * solve(i + 1, j + 1)) % MOD

            memo[i][j] = (skip + take) % MOD

            return memo[i][j]

        freq = [[0 for _ in range(len(words[0]))] for _ in range(26)]
        memo = [[-1 for _ in range(len(words[0]))] for _ in range(len(target))]
        MOD = 10**9 + 7

        for j in range(len(words[0])):
            for word in words:
                freq[ord(word[j]) - ord("a")][j] += 1

        return solve(0, 0)
