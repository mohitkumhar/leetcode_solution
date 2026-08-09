class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        def solve(player, i, M):
            if i >= n:
                return 0

            if (player, i, M) in memo:
                return memo[(player, i, M)]

            stones = 0

            if player == 1:
                result = 0
            else:
                result = float("inf")

            for x in range(1, 2 * M + 1):
                if i + x > n:
                    break

                stones += piles[x + i - 1]
                if player == 1:
                    result = max(result, stones + solve(0, i + x, max(M, x)))
                else:
                    result = min(result, solve(1, i + x, max(M, x)))

            memo[(player, i, M)] = result
            return result

        memo = {}
        return solve(1, 0, 1)
