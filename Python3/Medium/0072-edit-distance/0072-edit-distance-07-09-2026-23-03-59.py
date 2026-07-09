class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def solve(i: int, j: int) -> int:
            if i >= m:
                return n - j
            if j >= n:
                return m - i
            if memo[i][j] != -1:
                return memo[i][j]

            result = 0
            if word1[i] == word2[j]:
                result += solve(i + 1, j + 1)

            else:
                result += 1 + min(solve(i, j + 1), solve(i + 1, j), solve(i + 1, j + 1))

            memo[i][j] = result
            return result

        m = len(word1)
        n = len(word2)
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return solve(0, 0)
