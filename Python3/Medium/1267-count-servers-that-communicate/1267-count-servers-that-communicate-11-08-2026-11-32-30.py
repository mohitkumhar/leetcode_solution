class Solution:
    def countServers(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        count = 0

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue

                if grid[i][j] == 1:

                    queue = [(i, j)]
                    visited.add((i, j))

                    group_server = 0
                    while queue:
                        x, y = queue.pop(0)
                        group_server += 1

                        for row in range(m):
                            newX = row
                            newY = y
                            if grid[newX][newY] == 1 and (newX, newY) not in visited:
                                visited.add((newX, newY))
                                queue.append((newX, newY))

                        for col in range(n):
                            newX = x
                            newY = col

                            if grid[newX][newY] == 1 and (newX, newY) not in visited:
                                visited.add((newX, newY))
                                queue.append((newX, newY))

                    if group_server > 1:
                        count += group_server

        return count


# [[1,0,0,1,0]
#  [0,0,0,0,0]
#  [0,0,0,1,0]]
