class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        m = len(grid)
        n = len(grid[0])
        k %= m * n
        flatten_grid = []

        for i in range(m):
            for j in range(n):
                flatten_grid.append(grid[i][j])

        reverse(flatten_grid, 0, m * n - 1)
        reverse(flatten_grid, 0, k - 1)
        reverse(flatten_grid, k, m * n - 1)

        idx = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = flatten_grid[idx]
                idx += 1

        return grid
