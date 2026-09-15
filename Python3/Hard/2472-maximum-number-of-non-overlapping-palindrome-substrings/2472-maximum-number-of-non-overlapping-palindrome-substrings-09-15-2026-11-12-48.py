class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPal = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        for L in range(1, n + 1):
            i = 0
            while i + L - 1 < n:
                j = i + L - 1

                if L == 1:
                    isPal[i][j] = True
                elif L == 2:
                    isPal[i][j] = True if s[i] == s[j] else False
                else:
                    isPal[i][j] = s[i] == s[j] and isPal[i + 1][j - 1] == True
                i += 1

        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if j - i + 1 >= k and isPal[i][j]:
                    # including curr str in answer
                    take = 1
                    if j + k <= n:
                        take = 1 + dp[j + 1][j + k]

                    # increase size of palendrome(incremenet j)
                    inc = dp[i][j + 1]

                    # moving window 1 forward
                    incWind = dp[i + 1][j + 1]

                    dp[i][j] = max(take, inc, incWind)

                # increase size of palendrome(incremenet j)
                inc = dp[i][j + 1]

                # increase size of palendrome(incremenet j)
                incWind = dp[i + 1][j + 1]

                dp[i][j] = max(dp[i][j], inc, incWind)

        return dp[0][k - 1]
