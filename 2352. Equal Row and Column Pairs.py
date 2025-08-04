class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                match = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        match = False
                        break
                if match:
                    count += 1
        return count
