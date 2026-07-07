class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 7 + 10 ** 9
        def solve(idx, max_val, total_search):
            if idx == n:
                if total_search == k:
                    return 1
                return 0
            
            if total_search > k:
                return 0

            if memo[total_search][idx][max_val + 1] != -1:
                return memo[total_search][idx][max_val + 1]


            result = 0
            for i in range(m):
                if i > max_val:
                    result = (result + solve(idx + 1, i, total_search + 1)) % MOD
                else:
                    result = (result + solve(idx + 1, max_val, total_search)) % MOD

            memo[total_search][idx][max_val + 1] = result
            return result

        memo = [[[-1 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(k + 1)]

        return solve(0, -1, 0)
