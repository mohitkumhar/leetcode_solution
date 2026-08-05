class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if j >= i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for mat in matrix:
            mat.reverse()
