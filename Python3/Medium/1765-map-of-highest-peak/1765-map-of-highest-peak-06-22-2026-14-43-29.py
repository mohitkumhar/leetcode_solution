from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        neighbour = [[0,1], [1,0], [0,-1], [-1,0]]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))

        visited = set()

        while queue:
            x, y, curr_peak = queue.popleft()

            if (x, y) in visited:
                continue
            visited.add((x, y))

            isWater[x][y] = curr_peak

            for nei in neighbour:
                newX = x + nei[0]
                newY = y + nei[1]

                if 0 <= newX < m and 0 <= newY < n:
                    if (newX, newY) not in visited:
                        queue.append((newX, newY, curr_peak + 1))

        return isWater
