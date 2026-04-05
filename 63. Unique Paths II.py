class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.unique = 0
        table = {}

        def solve(i, j):
            if (i, j) in table:
                return table[(i,j)]
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1

            self.unique = solve(i + 1, j) + solve(i, j + 1)
            table[(i,j)] = self.unique
            return self.unique

        return solve(0,0)
