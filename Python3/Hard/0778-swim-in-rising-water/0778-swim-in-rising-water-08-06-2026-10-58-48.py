class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def isPossible(maxWater):
            queue = [(0, 0)]
            visited = set()
            visited.add((0, 0))
            
            if grid[0][0] > maxWater:
                return False

            while queue:
                x, y = queue.pop(0)

                if x == (n - 1) and y == (n - 1):
                    return True

                for dirx, diry in directions:
                    newX = dirx + x
                    newY = diry + y

                    if (
                        newX >= 0
                        and newX < n
                        and newY >= 0
                        and newY < n
                        and (newX, newY) not in visited
                    ):
                        if grid[newX][newY] <= maxWater:
                            queue.append((newX, newY))
                            visited.add((newX, newY))
            return False

        left = 0
        right = 2501
        result = -1
        n = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
