class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def adjecent_side(i, j):
            
            cells = [[i-1, j], [i, j-1], [i+1,j], [i, j+1]]
            pick = 0
            
            for x, y in cells:
                if(x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0):
                    pick += 1
            return pick



        result = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result += adjecent_side(i, j)
        
        return result
        