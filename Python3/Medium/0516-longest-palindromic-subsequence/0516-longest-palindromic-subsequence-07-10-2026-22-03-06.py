class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def solve(i, j):
            if i >= n or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            ans = 0
            if str1[i] == str2[j]:
                ans += 1 + solve(i + 1, j + 1)
            else:
                ans += max(solve(i + 1, j), solve(i, j + 1))

            memo[i][j] = ans
            return ans

        str1 = s
        str2 = s[::-1]
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        return solve(0, 0)
