class Solution:
    def nthUglyNumber(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[1] = 1

        i2 = 1
        i3 = 1
        i5 = 1

        for i in range(2, n + 1):
            i2_ugly = dp[i2] * 2

            i3_ugly = dp[i3] * 3

            i5_ugly = dp[i5] * 5

            dp[i] = min(i2_ugly, i3_ugly, i5_ugly)

            if dp[i] == i2_ugly:
                i2 += 1

            if dp[i] == i3_ugly:
                i3 += 1

            if dp[i] == i5_ugly:
                i5 += 1

        return dp[n]
