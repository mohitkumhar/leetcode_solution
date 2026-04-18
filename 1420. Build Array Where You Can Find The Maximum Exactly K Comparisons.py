class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[-1 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]

        def solve(idx, search_cost, max_value):
            if idx == n:
                if search_cost == k:
                    return 1
                else:
                    return 0

            if search_cost > k:
                return 0

            if dp[idx][search_cost][max_value] != -1:
                return dp[idx][search_cost][max_value]

            result = 0
            for i in range(1, m + 1):
                if i > max_value:
                    result = (result + solve(idx + 1, search_cost + 1, i)) % MOD
                else:
                    result = (result + solve(idx + 1, search_cost, max_value)) % MOD

            dp[idx][search_cost][max_value] = result

            return result

        return solve(0, 0, 0)
