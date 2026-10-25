class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = []
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0 and (i, j) not in visited:
                    queue = []
                    queue = [(i, j)]
                    is_not_boundary = True

                    while queue:
                        x, y = queue.pop(0)

                        if (x, y) in visited:
                            continue
                        visited.add((x, y))

                        if x == 0 or y == 0 or x == m-1 or y == n-1:
                            is_not_boundary = False

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == 0:
                                queue.append((newX, newY))

                    if is_not_boundary:
                        count += 1

        return count
