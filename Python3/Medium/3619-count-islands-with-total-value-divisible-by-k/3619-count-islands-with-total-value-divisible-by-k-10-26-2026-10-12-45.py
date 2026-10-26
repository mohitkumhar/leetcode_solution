class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        count = 0
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        for i in range(m):
            queue = []

            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in seen:
                    queue.append((i, j))
                    seen.add((i, j))
                    total = 0

                    while queue:
                        x, y = queue.pop(0)
                        total += grid[x][y]

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if ( 0 <= newX < m and 0 <= newY < n and (newX, newY) not in seen ):
                                if grid[newX][newY] != 0:
                                    seen.add((newX, newY))
                                    queue.append((newX, newY))

                    if total % k == 0:
                        count += 1

        return count
