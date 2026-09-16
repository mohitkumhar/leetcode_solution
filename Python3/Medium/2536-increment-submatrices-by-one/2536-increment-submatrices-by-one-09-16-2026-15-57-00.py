class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for query in queries:
            rowx, colx, rowy, coly = query

            for i in range(rowx, rowy + 1):
                mat[i][colx] += 1

                if coly + 1 < n:
                    mat[i][coly + 1] -= 1

        for i in range(n):
            cumSum = 0
            for j in range(n):
                cumSum += mat[i][j]
                mat[i][j] = cumSum

        return mat
