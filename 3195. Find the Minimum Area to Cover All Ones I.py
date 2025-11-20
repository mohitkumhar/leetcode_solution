class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        rmin = row_len
        cmin = col_len

        rmax = -1
        cmax = -1

        for i in range(row_len):
            row = grid[i]
            for j, col_val in enumerate(row):
                if col_val == 1:
                    if i > rmax: rmax = i
                    if i < rmin: rmin = i
                    if j > cmax: cmax = j
                    if j < cmin: cmin = j

            length  = rmax - rmin + 1
            width   = cmax - cmin + 1

        return length * width
