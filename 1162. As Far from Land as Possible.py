class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        queue = []
        answer = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        if not queue or len(queue) == m*n:
            return -1

        while queue:
            x, y, distance = queue.pop(0)
            answer = max(answer, distance)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if newX >= 0 and newX < m and newY >= 0 and newY < n:
                    if grid[newX][newY] == 0 and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        queue.append((newX, newY, distance + 1))

        return answer
