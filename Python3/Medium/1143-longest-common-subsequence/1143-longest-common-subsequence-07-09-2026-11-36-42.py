class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        def solve(i, j):
            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            result = 0
            if text1[i] == text2[j]:
                result += 1 + solve(i + 1, j + 1)
            else:
                result += max(solve(i + 1, j), solve(i, j + 1))

            memo[i][j] = result
            return result

        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        return solve(0, 0)
