class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        neighbour = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        visited = set()
        total_time = 0

        while queue:
            x, y, dist = queue.pop(0)
            total_time = max(total_time, dist)

            for nei in neighbour:
                newX = x + nei[0]
                newY = y + nei[1]

                if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == 1:
                    grid[newX][newY] = 2
                    queue.append((newX, newY, dist + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return total_time
