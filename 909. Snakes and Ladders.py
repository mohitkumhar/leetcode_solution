class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def pos_to_cord(pos, n):
            idx = pos - 1
            row_from_bottom = idx // n
            row = n - 1 - row_from_bottom

            col = idx % n
            if row_from_bottom % 2 == 1:
                col = n - 1 - col
            return row, col

        queue = [(1, 0)]
        n = len(board)
        visited = set()

        while queue:
            pos, rolls = queue.pop(0)

            if pos in visited:
                continue
            visited.add(pos)

            if pos == n*n:
                return rolls

            for i in range(1, 7):
                v = pos + i

                if v > n*n:
                    continue

                row, col = pos_to_cord(v, n)

                if board[row][col] != -1:
                    v = board[row][col]

                if v not in visited:
                    queue.append((v, rolls + 1))

        return -1
