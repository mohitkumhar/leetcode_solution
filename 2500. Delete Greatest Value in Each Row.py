class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)

        col = len(grid[0])
        result = 0

        for i in range(0, col):
            max_value = 0
            for row in grid:
                max_value = max(max_value, row[i])
            result += max_value
        return result
