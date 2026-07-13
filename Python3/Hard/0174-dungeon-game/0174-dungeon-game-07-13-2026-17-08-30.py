class Solution:
    def solve(
        self,
        i: int,
        j: int,
        m: int,
        n: int,
        dungeon: List[List[ing]],
        memo: List[List[int]],
    ) -> int:
        if i >= m or j >= n:
            return float("inf")
        if i == m - 1 and j == n - 1:
            if dungeon[i][j] < 0:
                return abs(dungeon[i][j]) + 1
            return 1
        if memo[i][j] != -1:
            return memo[i][j]

        down = self.solve(i + 1, j, m, n, dungeon, memo)
        right = self.solve(i, j + 1, m, n, dungeon, memo)

        if min(down, right) - dungeon[i][j] <= 0:
            memo[i][j] = 1
            return 1
        memo[i][j] = min(down, right) - dungeon[i][j]
        return memo[i][j]

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solve(0, 0, m, n, dungeon, memo)
