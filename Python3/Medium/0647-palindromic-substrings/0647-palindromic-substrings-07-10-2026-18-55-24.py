class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        i = 0
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        for L in range(1, n + 1):
            i = 0
            while (L + i - 1) < n:
                j = L + i - 1

                if (j - i + 1) == 1:
                    dp[i][j] = True
                elif (j - i + 1) == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == True:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False

                if dp[i][j]:
                    count += 1

                i += 1
        return count
