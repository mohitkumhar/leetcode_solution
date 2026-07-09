class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m = len(str1)
        n = len(str2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        i = m
        j = n
        result = []

        while i > 0 or j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    result.append(str1[i - 1])
                    i -= 1
                else:
                    result.append(str2[j - 1])
                    j -= 1

        return ''.join(result[::-1])
