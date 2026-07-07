class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        ans = 1

        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    if (dp[j] + 1) > dp[i]:
                        dp[i] = dp[j] + 1
                        ans = max(ans, dp[i])

        return ans
