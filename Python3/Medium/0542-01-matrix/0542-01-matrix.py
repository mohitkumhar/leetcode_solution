from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(mat)
        n = len(mat[0])
        neighbour = [[1,0], [0,1], [0,-1], [-1,0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            x, y = queue.popleft()

            for nei in neighbour:
                newX = x + nei[0]
                newY = y + nei[1]

                if 0 <= newX < m and 0 <= newY < n:
                    if mat[newX][newY] == -1:
                        mat[newX][newY] = mat[x][y] + 1
                        queue.append((newX, newY))

        return mat
