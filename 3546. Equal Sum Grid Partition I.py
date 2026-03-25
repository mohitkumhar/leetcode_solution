class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowSum = []
        colSum = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            temp = 0
            for j in range(n):
                temp += grid[i][j]
            rowSum.append(temp)

        for j in range(n):
            temp = 0
            for i in range(m):
                temp += grid[i][j]
            colSum.append(temp)

        totalSum = sum(sum(row) for row in grid)

        currRowSum = 0
        for i in range(m):
            currRowSum += rowSum[i]
            if currRowSum == totalSum - currRowSum:
                return True

        currColSum = 0
        for i in range(n):
            currColSum += colSum[i]
            if currColSum == totalSum - currColSum:
                return True

        return False
