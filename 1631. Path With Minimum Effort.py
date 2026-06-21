import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        neighbor = [[1,0], [0,1], [0,-1], [-1,0]]

        efforts = [[float('inf') for _ in range(n)] for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            dist, i, j = heapq.heappop(heap)

            for x, y in neighbor:
                newX = i + x
                newY = j + y

                if 0 <= newX < m and 0 <= newY < n:
                    curr_efforts = abs(heights[i][j] - heights[newX][newY])
                    curr_efforts = max(curr_efforts, dist)

                    if efforts[newX][newY] > curr_efforts:
                        efforts[newX][newY] = curr_efforts
                        heapq.heappush(heap, (curr_efforts, newX, newY))

        return efforts[m-1][n-1]
