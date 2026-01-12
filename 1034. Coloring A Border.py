class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        queue = [(row, col)]
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        result = []
        m = len(grid)
        n = len(grid[0])
        original_color = grid[row][col]

        while queue:
            x, y = queue.pop(0)
            visited.add((x, y))
            is_border = False

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if newX < 0 or newX >= m or newY < 0 or newY >= n:
                    is_border = True

                elif grid[newX][newY] != original_color:
                    is_border = True

                elif grid[newX][newY] == original_color and (newX, newY) not in visited:
                    queue.append((newX, newY))

            if is_border:
                result.append((x, y))

        for x, y in result:
            grid[x][y] = color

        return grid
