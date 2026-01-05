class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        rows = len(mat)
        cols = len(mat[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            x, y = queue.pop(0)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if newX >= 0 and newX < rows and newY >= 0 and newY < cols:
                    if mat[newX][newY] == -1:
                        mat[newX][newY] = mat[x][y] + 1
                        queue.append((newX, newY))

        return mat
