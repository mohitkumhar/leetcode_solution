class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 10**9 + 7
        memo = [[[-1 for _ in range(maxMove + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j, moves):
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            
            if moves == 0:
                return 0

            if memo[i][j][moves] != -1:
                return memo[i][j][moves]
            
            ans = 0
            
            ans += solve(i + 1, j, moves - 1)
            ans += solve(i, j + 1, moves - 1)
            
            ans += solve(i - 1, j, moves - 1)
            ans += solve(i, j - 1, moves - 1)
            
            memo[i][j][moves] = ans % MOD

            return ans % MOD
        ans = solve(startRow, startColumn, maxMove)
        return ans % MOD
