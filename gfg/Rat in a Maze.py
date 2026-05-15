class Solution:
    def ratInMaze(self, maze):
        m = len(maze)
        n = len(maze[0])
        self.result = []

        def solve(i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if i == m - 1 and j == n - 1:
                self.result.append(''.join(path))
                return

            if maze[i][j] == 0:
                return
            
            maze[i][j] = 0
            
            # Down
            path.append("D")
            solve(i + 1, j, path)
            path.pop()
            
            # Left
            path.append("L")
            solve(i, j - 1, path)
            path.pop()
            
            # Right
            path.append("R")
            solve(i, j + 1, path)
            path.pop()
            
            # Up
            path.append("U")
            solve(i - 1, j, path)
            path.pop()
            
            maze[i][j] = 1
        
        solve(0,0,[])
        
        return self.result
