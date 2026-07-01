class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        dist = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()

            for nei in neighbours:
                newX = x + nei[0]
                newY = y + nei[1]

                if 0 <= newX < m and 0 <= newY < n and dist[newX][newY] == -1:
                    dist[newX][newY] = dist[x][y] + 1
                    queue.append((newX, newY))

        left = 0
        right = 401
        ans = 0

        while left < right:
            mid = left + (right - left) // 2
            queue = deque()
            visited = set()

            if dist[0][0] >= mid:
                queue.append((0, 0))
                visited.add((0, 0))

                while queue:
                    x, y = queue.popleft()

                    if x == (m-1) and y == (n-1):
                        ans = mid

                    for nei in neighbours:
                        newX = x + nei[0]
                        newY = y + nei[1]

                        if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                            visited.add((newX, newY))
                            if dist[newX][newY] >= mid:
                                queue.append((newX, newY))

            if ans == mid:
                left = mid + 1
            else:
                right = mid

        return ans
