class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        def solve(start):
            if start >= n:
                return 1

            if memo[start] != -1:
                return memo[start]

            ans = 0
            for end in range(start, n):
                newStr = s[start : end + 1]

                if int(newStr) in range(1, k + 1):
                    ans = (ans + solve(end + 1)) % MOD
                else:
                    break

            memo[start] = ans
            return memo[start] % MOD

        n = len(s)
        MOD = 10**9 + 7
        memo = [-1 for _ in range(n + 1)]

        return solve(0)
