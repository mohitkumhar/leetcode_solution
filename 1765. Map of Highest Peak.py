class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        queue = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 0:
                    isWater[i][j] = -1
                else:
                    queue.append((i, j))
                    isWater[i][j] = 0

        while queue:
            x, y = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if 0 <= newX < m and 0 <= newY < n:
                    if (newX, newY) not in visited and isWater[newX][newY] == -1:
                        isWater[newX][newY] = isWater[x][y] + 1
                        queue.append((newX, newY))

        return isWater
