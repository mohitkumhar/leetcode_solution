class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        def solve(i, j):
            if i > j:
                memo[i][j] = True
                return True
            if memo[i][j] != -1:
                return memo[i][j]

            if s[i] == s[j]:
                ans = solve(i + 1, j - 1)
                memo[i][j] = ans
                return ans
            else:
                memo[i][j] = False
                return False

        count = 0
        for i in range(n):
            for j in range(i, n):
                if solve(i, j):
                    count += 1
        return count
