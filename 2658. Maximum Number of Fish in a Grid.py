class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        queue = []
        visited = set()
        answer = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):

                if grid[i][j] != 0 and (i, j) not in visited:
                    queue.append((i, j))
                    temp = 0

                    while queue:
                        x, y = queue.pop(0)
                        if (x, y) in visited:
                            continue
                        visited.add((x, y))

                        temp += grid[x][y]
                        answer = max(answer, temp)

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if newX >= 0 and newX < m and newY >= 0 and newY < n:
                                if grid[newX][newY] != 0 and (newX, newY) not in visited:
                                    queue.append((newX, newY))
        return answer
