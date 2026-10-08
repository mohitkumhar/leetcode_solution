class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:

        def solve(i, k):
            if i >= n:
                return 0

            if memo[i][k] != -1:
                return memo[i][k]

            notTake = solve(i + 1, k)

            take = 0
            sum = 0

            for j in range(min(len(piles[i]), k)):
                sum += piles[i][j]

                if (k - (j + 1)) >= 0:
                    take = max(take, sum + solve(i + 1, k - (j + 1)))

            memo[i][k] = max(notTake, take)
            return memo[i][k]

        n = len(piles)
        memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

        return solve(0, k)
