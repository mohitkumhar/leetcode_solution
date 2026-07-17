class Solution:
    def __init__(self):
        self.count = 0
        self.empty_path = 0
        self.start_point = (0, 0)
        self.directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        self.m = 0
        self.n = 0

    def backtrack(self, i: int, j: int, curr_path: int, grid: List[List[int]]):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] == -1:
            return

        if grid[i][j] == 2:
            if curr_path == self.empty_path:
                self.count += 1
            return

        grid[i][j] = -1
        for dirx, diry in self.directions:
            newI = i + dirx
            newJ = j + diry
            self.backtrack(newI, newJ, curr_path + 1, grid)

        grid[i][j] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.start_point = (i, j)
                if grid[i][j] == 0:
                    self.empty_path += 1

        self.empty_path += 1
        self.backtrack(self.start_point[0], self.start_point[1], 0, grid)

        return self.count
