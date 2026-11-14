class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        heap = []

        visited = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        ans = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while heap:
            height, x, y = heapq.heappop(heap)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                    ans += max(0, height - heightMap[newX][newY])
                    heapq.heappush(
                        heap, (max(height, heightMap[newX][newY]), newX, newY)
                    )
                    visited.add((newX, newY))

        return ans
