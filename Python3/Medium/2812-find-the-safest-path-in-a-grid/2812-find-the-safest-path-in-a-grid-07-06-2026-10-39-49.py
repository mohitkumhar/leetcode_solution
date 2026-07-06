class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        distance = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    distance[i][j] = 0
        
        while queue:
            x, y = queue.popleft()

            for dirx, diry in directions:
                newX = x + dirx
                newY = y + diry

                if newX < m and newX >= 0 and newY < n and newY >= 0 and distance[newX][newY] == -1:
                   distance[newX][newY] = distance[x][y] + 1
                   queue.append((newX, newY))

        left = 0
        right = 401
        safest_path = 0

        while left < right:
            mid = left + (right - left) // 2

            queue = deque()
            visited = set()

            if distance[0][0] >= mid:
                queue.append((0, 0))
                visited.add((0, 0))

                while queue:
                    x, y = queue.popleft()

                    if x == (m-1) and y == (n-1):
                        safest_path = mid

                    for dirx, diry in directions:
                        newX = x + dirx
                        newY = y + diry

                        if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                            visited.add((newX, newY))
                            if distance[newX][newY] >= mid:
                                queue.append((newX, newY))

            if safest_path == mid:
                left = mid + 1
            else:
                right = mid

        return safest_path
