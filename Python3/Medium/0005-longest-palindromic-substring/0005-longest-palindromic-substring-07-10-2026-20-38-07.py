class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_pal = ""

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

                if dp[i][j] == True:
                    if L > len(max_pal):
                        max_pal = s[i:j+1]
                i+=1

        return max_pal
