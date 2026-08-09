class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = [[-1 for _ in range(12 + 1)] for _ in range(n + 1)]

        def solve(n, prev):

            if n == 0:
                return 1
            if memo[n][prev] != -1:
                return memo[n][prev]

            result = 0
            last = possibleComb[prev]

            for i in range(12):
                curr = possibleComb[i]
                if curr == last:
                    continue

                conflict = False
                for j in range(3):
                    if curr[j] == last[j]:
                        conflict = True
                        break

                if not conflict:
                    result = result + (solve(n - 1, i) % MOD)

            memo[n][prev] = result
            return result

        possibleComb = [
            "ryr",
            "yry",
            "gry",
            "ryg",
            "yrg",
            "grg",
            "rgr",
            "ygr",
            "gyr",
            "rgy",
            "ygy",
            "gyg",
        ]

        result = 0
        for i in range(12):
            result = result + (solve(n - 1, i) % MOD)

        return result % MOD
