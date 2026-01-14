class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue_island_one = []
        queue = []
        visited = set()
        found_island = False
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(m):
            if found_island:
                break
            for j in range(n):

                if grid[i][j] == 1:
                    found_island=True
                    queue.append((i, j))
                    queue_island_one.append((i, j, 0))

                    while queue:
                        x, y = queue.pop(0)

                        if (x, y) in visited:
                            continue
                        visited.add((x, y))

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if newX >= 0 and newX < m and newY >= 0 and newY < n:
                                if grid[newX][newY] == 1:
                                    queue.append((newX, newY))
                                    queue_island_one.append((newX, newY, 0))
                    break

        water_visited = set()

        while queue_island_one:
            x, y, distance = queue_island_one.pop(0)

            if grid[x][y] == 0 and (x, y) in water_visited:
                continue
            elif grid[x][y] == 0:
                water_visited.add((x, y))

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if newX >= 0 and newX < m and newY >= 0 and newY < n:
                    if grid[newX][newY] == 0:
                        queue_island_one.append((newX, newY, distance + 1))

                    elif grid[newX][newY] == 1 and (newX, newY) not in visited:
                        return distance
