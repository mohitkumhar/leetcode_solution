class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def find_distance(x1: int, y1: int, x2: int, y2: int) -> int:
            return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

        queue = [(entrance[0], entrance[1], 0)]
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        min_distance = float('inf')
        m = len(maze)
        n = len(maze[0])
        visited = set()

        while queue:
            x, y, distance = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == 0 or x == m-1 or y == 0 or y == n-1:
                if [x,y] != entrance:
                    return distance

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if 0 <= newX < m and 0 <= newY < n:
                    if maze[newX][newY] == "." and (newX, newY) not in visited:
                        queue.append((newX, newY, distance + 1))

        return -1
