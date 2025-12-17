class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(x, y, rows, cols):
            return x >= 0 and x < rows and y >= 0 and y < cols

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        count = 0
        temp_queue = []

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1":
                    count += 1

                    
                    temp_queue.append((i, j))

                    while temp_queue:

                        values = temp_queue.pop()

                        x, y = values[0], values[1]

                        grid[x][y] = "0"

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]


                            if isValid(newX, newY, m, n) and grid[newX][newY] == '1':
                                temp_queue.append((newX, newY))

        return count
