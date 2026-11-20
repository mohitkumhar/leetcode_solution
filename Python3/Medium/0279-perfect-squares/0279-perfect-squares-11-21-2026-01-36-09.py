class Solution:
    def numSquares(self, n: int) -> int:

        def helper(n):
            if n <= 0:
                return 0
            if memo[n] != -1:
                return memo[n]

            minCount = float("inf")

            i = 1
            while i * i <= n:
                result = 1 + helper(n - i * i)
                minCount = min(minCount, result)
                i += 1

            memo[n] = minCount
            return memo[n]

        memo = [-1] * (n + 1)
        return helper(n)
