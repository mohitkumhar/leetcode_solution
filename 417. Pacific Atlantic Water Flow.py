class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isValid(x, y, row, col):
            return x >= 0 and x < row and y >= 0 and  y < col

        queue = []
        visited = set()
        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    queue.append((i, j))
                    visited.add((i, j))

                if j == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        queue = list(set(queue))
        pacific = []
        pacific.extend(queue)

        while queue:
            x, y = queue.pop(0)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if (newX, newY) not in visited and isValid(newX, newY, m, n) and heights[x][y] <= heights[newX][newY]:
                    queue.append((newX, newY))
                    visited.add((newX, newY))
                    pacific.append((newX, newY))

        queue = []
        visited = set()

        for i in range(m):
            for j in range(n):                
                if j == (n - 1):
                    queue.append((i, j))
                    visited.add((i, j))

                if i == (m - 1):
                    queue.append((i, j))
                    visited.add((i, j))
        
        queue = list(set(queue))
        atlantic = []
        atlantic.extend(queue)

        while queue:
            x, y = queue.pop(0)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if (newX, newY) not in visited and isValid(newX, newY, m, n) and heights[x][y] <= heights[newX][newY]:
                    queue.append((newX, newY))
                    visited.add((newX, newY))
                    atlantic.append((newX, newY))

        pacific = set(pacific)
        result = []
        for a in atlantic:
            if a in pacific:
                result.append(a)
        
        return result
