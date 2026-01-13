class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maximum = 0
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        visited = set()

        for i in range(m):
            for j in range(n):
                queue = []
                temp = 0

                if grid[i][j] == 1 and (i, j) not in visited:
                    queue.append((i, j))

                    while queue:
                        x, y = queue.pop(0)

                        if (x, y) in visited:
                            continue
                        visited.add((x, y))

                        temp += 1

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if newX >= 0 and newX < m and newY >= 0 and newY < n:
                                if grid[newX][newY] == 1 and (newX, newY) not in visited:
                                    queue.append((newX, newY))

                    maximum = max(maximum, temp)

        return maximum
