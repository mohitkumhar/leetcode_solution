class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def isPossible(day):
            grid = [[0] * col for _ in range(row)]

            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            queue = deque()

            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue:
                r, c = queue.popleft()

                if r == row - 1:
                    return True

                for direction in directions:
                    newR = r + direction[0]
                    newC = c + direction[1]

                    if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == 0:
                        grid[newR][newC] = 1
                        queue.append((newR, newC))

            return False

        left = 0
        right = len(cells)
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
