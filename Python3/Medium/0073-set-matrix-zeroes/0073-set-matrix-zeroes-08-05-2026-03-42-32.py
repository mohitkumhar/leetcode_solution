class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def setRowZero(x):
            for i in range(n):
                matrix[x][i] = 0

        def setColZero(y):
            for i in range(m):
                matrix[i][y] = 0

        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    print(i, j)
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            setRowZero(row)
        for col in cols:
            setColZero(col)
