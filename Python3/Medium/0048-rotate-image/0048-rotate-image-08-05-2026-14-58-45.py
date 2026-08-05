class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if j >= i: # or start j loop from 1
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for mat in matrix:
            mat.reverse()
