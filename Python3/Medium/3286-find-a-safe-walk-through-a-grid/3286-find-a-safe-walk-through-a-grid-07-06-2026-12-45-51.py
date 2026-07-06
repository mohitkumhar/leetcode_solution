class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = deque()
        health -= grid[0][0]
        if health <= 0:
            return False
        queue.append((0, 0, health))
        visited = {(0,0, health)}

        while queue:
            x, y, hel = queue.popleft()
            
            if x == (m-1) and y == (n-1) and hel > 0:
                return True

            for dirx, diry in directions:
                newX = x + dirx
                newY = y + diry

                if 0 <= newX < m and 0 <= newY < n:
                    temp = hel - grid[newX][newY]
                    if temp > 0 and (newX, newY, temp) not in visited:
                        visited.add((newX, newY, temp))
                        queue.append((newX, newY, temp))

        return False
