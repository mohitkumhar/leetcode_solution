from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        neighbour = [[1,0], [0,1], [0,-1], [-1,0]]

        while queue:
            x, y, dist = queue.popleft()

            if x == 0 or x == (m - 1) or y == 0 or y == (n - 1):
                if [x, y] != entrance:
                    return dist

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nei in neighbour:
                newX = x + nei[0]
                newY = y + nei[1]

                if 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == ".":
                    if (newX, newY) not in visited:
                        queue.append((newX, newY, dist + 1))

        return -1
