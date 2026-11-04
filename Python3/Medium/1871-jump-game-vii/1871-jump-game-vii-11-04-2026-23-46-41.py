class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [0] * n
        dp[0] = 1

        count = 0

        for i in range(1, n):

            if (i - minJump) >= 0:
                count += dp[i - minJump]

            if (i - maxJump - 1) >= 0:
                count -= dp[i - maxJump - 1]

            if count > 0 and s[i] == "0":
                dp[i] = count

        return True if dp[n - 1] > 0 else False
