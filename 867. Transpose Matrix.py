class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        columns = len(matrix[0])

        result = [[None] * rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                result[j][i] = matrix[i][j]

        return result
