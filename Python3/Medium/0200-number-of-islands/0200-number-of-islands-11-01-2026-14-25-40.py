class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        m = len(grid)
        n = len(grid[0])

        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    queue = [(i, j)]
                    seen.add((i, j))

                    while queue:
                        x, y = queue.pop(0)

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if (
                                0 <= newX < m
                                and 0 <= newY < n
                                and grid[newX][newY] == "1"
                            ):
                                if (newX, newY) not in seen:
                                    seen.add((newX, newY))
                                    queue.append((newX, newY))

                    count += 1

        return count
