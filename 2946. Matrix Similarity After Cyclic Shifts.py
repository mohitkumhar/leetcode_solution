class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        org_mat = [rows[:] for rows in mat]
        m = len(mat)
        n = len(mat[0])
        k = k % n

        for i in range(m):
            if i % 2 == 0:
                #  for even
                temp = k
                while temp != 0:
                    first = mat[i][0]
                    for x in range(len(mat[i]) - 1):
                        mat[i][x] = mat[i][x + 1]
                    mat[i][-1] = first
                    temp -= 1

            else:
                #  for odd
                temp = k
                while temp != 0:
                    first = mat[i][0]
                    for x in range(len(mat[i]) - 1):
                        mat[i][x] = mat[i][x + 1]
                    mat[i][-1] = first
                    temp -= 1

        return org_mat == mat
