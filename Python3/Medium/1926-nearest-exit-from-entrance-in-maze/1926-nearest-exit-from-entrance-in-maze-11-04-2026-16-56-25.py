class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))

        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while queue:
            x, y, dist = queue.popleft()

            if (x == m - 1 or y == n - 1 or x == 0 or y == 0) and dist > 0:
                return dist

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if (
                    0 <= newX < m
                    and 0 <= newY < n
                    and (newX, newY) not in visited
                    and maze[newX][newY] == "."
                ):
                    visited.add((newX, newY))
                    queue.append((newX, newY, dist + 1))

        return -1
