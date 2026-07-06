class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        distance = [[float('inf') for _ in range(n)] for _ in range(m)] 
        distance[0][0] = grid[0][0]
        print(distance)

        heap = [(grid[0][0], 0, 0)]

        while heap:
            curr_cost, x, y = heapq.heappop(heap)

            if curr_cost > distance[x][y]:
                continue
            
            for dirx, diry in directions:
                newX = x + dirx
                newY = y + diry

                if 0 <= newX < m and 0 <= newY < n:
                    new_cost = curr_cost + grid[newX][newY]
                    if new_cost >= distance[newX][newY]:
                        continue
                    distance[newX][newY] = new_cost
                    heapq.heappush(heap, (new_cost, newX, newY))

        return health - distance[m-1][n-1] >= 1


