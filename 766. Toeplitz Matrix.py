class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        rows_length = len(matrix)
        column_length = len(matrix[0])

        for i in range(1, rows_length):
            for j in range(1, column_length):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
