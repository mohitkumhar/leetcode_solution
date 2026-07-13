class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    if dungeon[i][j] < 0:
                        dp[i][j] = abs(dungeon[i][j]) + 1
                    else:
                        dp[i][j] = 1

                else:
                    curr_req = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                    if curr_req <= 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = curr_req

        return dp[0][0]
