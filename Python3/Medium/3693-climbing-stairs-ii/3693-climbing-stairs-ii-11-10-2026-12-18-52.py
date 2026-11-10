class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        def solve(i):
            if i == n:
                return 0

            if memo[i] != -1:
                return memo[i]

            jumpFirst = float("inf")
            if i + 1 <= n:
                j = i + 1
                jumpFirst = costs[j - 1] + (j - i) ** 2 + solve(j)

            jumpSecond = float("inf")
            if i + 2 <= n:
                j = i + 2
                jumpSecond = costs[j - 1] + (j - i) ** 2 + solve(j)

            jumpThird = float("inf")
            if i + 3 <= n:
                j = i + 3
                jumpThird = costs[j - 1] + (j - i) ** 2 + solve(j)

            memo[i] = min(jumpFirst, jumpSecond, jumpThird)
            return memo[i]

        memo = [-1] * n

        return solve(0)
