class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])

        for _ in range(4):
            for i in range(m):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

            if mat == target:
                return True

        return False
