class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = (len(grid))
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if i < rows - 1:
                    if not grid[i][j] == grid[i + 1][j]:
                        return False

                if j < cols - 1:
                    if not grid[i][j] != grid[i][j + 1]:
                        return False
        return True
