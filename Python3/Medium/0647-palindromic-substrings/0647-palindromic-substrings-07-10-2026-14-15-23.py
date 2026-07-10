class Solution:
    def countSubstrings(self, s: str) -> int:
        def solve(i: int, j: int) -> bool:
            if i > j:
                memo[i][j] = True
                return True
            
            if memo[i][j] != None:
                return memo[i][j]

            if s[i] == s[j]:
                memo[i][j] = solve(i + 1, j - 1)
                return memo[i][j]
            else:
                memo[i][j] = False
                return False

        n = len(s)
        count = 0
        memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(i, n):
                if solve(i, j):
                    count += 1
        return count
