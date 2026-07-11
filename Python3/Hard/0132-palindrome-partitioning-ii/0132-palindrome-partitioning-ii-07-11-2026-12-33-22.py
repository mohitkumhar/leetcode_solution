class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        for L in range(1, n + 1):
            i = 0
            while (i + L - 1) < n:
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                i += 1

        cuts_dp = [float("inf")] * n
        cuts_dp[0] = 0

        for i in range(n):
            if dp[0][i]:
                cuts_dp[i] = 0
            for k in range(i):
                if dp[k + 1][i] == True:
                    cuts_dp[i] = min(cuts_dp[i], cuts_dp[k] + 1)

        return cuts_dp[n - 1]
