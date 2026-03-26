class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = sum(sum(rows) for rows in grid)

        def check_hor_cut(grid):
            m = len(grid)
            n = len(grid[0])
            seen = set()
            top = 0

            for i in range(m-1):
                for j in range(n):
                    top += grid[i][j]
                    seen.add(grid[i][j])

                bottom = total_sum - top
                diff = top - bottom

                if diff == 0:
                    return True

                if diff == grid[0][0]:
                    return True

                if diff == grid[0][n - 1]:
                    return True

                if diff == grid[i][0]:
                    return True

                if i > 0 and n > 1 and diff in seen:
                    return True

            return False


        #  checking for horizontal cuts
        if check_hor_cut(grid):
            return True

        grid.reverse()

        if check_hor_cut(grid):
            return True

        grid.reverse()


        # checking for vertical cuts
        m = len(grid)
        n = len(grid[0])

        transpose_mat = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transpose_mat[j][i] = grid[i][j]


        if check_hor_cut(transpose_mat):
            return True

        transpose_mat.reverse()

        if check_hor_cut(transpose_mat):
            return True

        return False

