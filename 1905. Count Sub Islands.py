class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0
        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        m = len(grid1)
        n = len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited:

                    is_sub_island = True
                    queue = [(i, j)]

                    while queue:
                        x, y = queue.pop(0)
                        if (x, y) in visited:
                            continue
                        visited.add((x, y))

                        if grid1[x][y] == 0:
                            is_sub_island = False

                        for direction in directions:
                            newX = x + direction[0]
                            newY = y + direction[1]

                            if newX >= 0 and newX < m and newY >= 0 and newY < n:
                                if grid2[newX][newY] == 1:
                                    queue.append((newX, newY))
                    if is_sub_island:
                        count += 1

        return count

