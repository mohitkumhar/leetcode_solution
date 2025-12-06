class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(x, y, rows, cols):
            return (x >= 0 and x < rows and y >= 0 and y < cols)

        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = []
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            curr_orange = queue.pop(0)

            for direction in directions:
                newX = curr_orange[0] + direction[0]
                newY = curr_orange[1] + direction[1]
                time = curr_orange[2]

                if isValid(newX, newY, rows, cols) and grid[newX][newY] == 1:
                    queue.append((newX, newY, time + 1))
                    grid[newX][newY] = 2
                    time+= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return time
