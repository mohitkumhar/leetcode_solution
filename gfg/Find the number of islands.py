class Solution:
    def numIslands(self, grid):
        visited = set()
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "L" and (i, j) not in visited:
                    
                    queue = [(i, j)]
                    count += 1
                    
                    while queue:
                        x, y = queue.pop(0)
                        
                        if grid[x][y] == "L":
                            
                            if (x, y) in visited:
                                continue
                            visited.add((x, y))
                            
                            for nei in neighbours:
                                newX = x + nei[0]
                                newY = y + nei[1]
                                
                                if newX >= 0 and newX < m and newY >= 0 and newY < n and grid[newX][newY] == "L":
                                    queue.append((newX, newY))

        
        return count
