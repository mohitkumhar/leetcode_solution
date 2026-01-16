class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[n-1][n-1] != 0 or grid[0][0] != 0:
            return -1

        distances = [[0,1], [1,0], [0,-1], [-1,0], [-1,1], [1,1], [1,-1], [-1,-1]]
        visited = set()
        answer = 0
        queue = [(0,0, 1)]

        while queue:
            x, y, path = queue.pop(0)

            if (x, y) in visited:
                continue
            visited.add((x,y))

            if x == n-1 and y == n-1:
                return path

            for distance in distances:
                newX = x + distance[0]
                newY = y + distance[1]

                if newX >= 0 and newX < n and newY >= 0 and newY < n:
                    if grid[newX][newY] == 0 and (newX, newY) not in visited:
                        queue.append((newX, newY, path+1))

        return -1
