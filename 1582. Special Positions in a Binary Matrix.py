class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = {}
        column = {}
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if i not in row:
                    row[i] = 0
                if j not in column:
                    column[j] = 0

                if mat[i][j] == 1:
                    row[i] += 1
                    column[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if row[i] <= 1 and column[j] <= 1:
                        count += 1
        return count
