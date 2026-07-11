class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for L in range(1, n + 1):
            i = 0
            while (i + L - 1) < n:
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1] == True
                i+=1

        dp_cuts = [float("inf")] * n
        dp_cuts[0] = 0

        for i in range(n):
            if dp[0][i]:
                dp_cuts[i] = 0
            for k in range(i):
                if dp[k + 1][i]:
                    curr_cuts = 1 + dp_cuts[k]
                    dp_cuts[i] = min(dp_cuts[i], curr_cuts)

        return dp_cuts[n - 1]
