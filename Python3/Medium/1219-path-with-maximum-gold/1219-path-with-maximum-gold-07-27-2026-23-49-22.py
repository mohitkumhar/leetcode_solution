class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(grid, i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
                return 0

            max_gold = 0

            org_gold = grid[i][j]
            grid[i][j] = 0

            for dx, dy in directions:
                newX = i + dx
                newY = j + dy

                max_gold = max(max_gold, dfs(grid, newX, newY))

            grid[i][j] = org_gold

            return grid[i][j] + max_gold

        m = len(grid)
        n = len(grid[0])
        max_gold = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(grid, i, j))

        return max_gold
