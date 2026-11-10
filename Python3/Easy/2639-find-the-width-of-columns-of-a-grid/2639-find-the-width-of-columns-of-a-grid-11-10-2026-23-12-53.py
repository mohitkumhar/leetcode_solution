class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])

        ans = [0] * n

        for i in range(m):
            for j in range(n):
                ans[j] = max(ans[j], len(str(grid[i][j])))

        return ans
