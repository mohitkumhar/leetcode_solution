class Solution:
    def longestPalindrome(self, s: str) -> str:

        def solve(i: int, j: int) -> bool:
            if i >= j:
                memo[i][j] = 1
                return True

            if memo[i][j] != -1:
                return True if memo[i][j] == 1 else False

            if s[i] == s[j]:
                ans = solve(i + 1, j - 1)
                if ans == True:
                    memo[i][j] = 1
                else:
                    memo[i][j] = 0
                return ans
            else:
                memo[i][j] = 0
                return False

        n = len(s)
        ans = ""
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if solve(i, j):
                    if (j - i + 1) > len(ans):
                        ans = s[i: j+1]

        return ans
