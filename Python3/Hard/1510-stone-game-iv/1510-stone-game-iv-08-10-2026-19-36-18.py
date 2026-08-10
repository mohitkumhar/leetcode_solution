class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        def solve(n):
            if n == 0:
                return False
            if memo[n] != -1:
                return memo[n]

            for k in range(1, int(n**0.5) + 1):
                if solve(n - (k * k)) == False:  # calling for bob
                    memo[n] = True
                    return True

            memo[n] = False

            return False

        memo = [-1] * (n + 1)

        return solve(n)  # alice is playing, true if he wins else false
