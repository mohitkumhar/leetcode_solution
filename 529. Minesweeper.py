class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def isValid(x, y, num_row, num_col):
            return x >= 0 and x < num_row and y >= 0 and y < num_col

        directions = [
            [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1] 
            ]

        queue = []

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        queue.append((click[0], click[1]))
        visited = set()
        visited.add((click[0], click[1]))

        len_row = len(board)
        len_col = len(board[0])

        while queue:
            i, j = queue.pop(0)

            if board[i][j] == "E":
                mine_count = 0

                for direction in directions:
                    newI = i + direction[0]
                    newJ = j + direction[1]

                    if isValid(newI, newJ, len_row, len_col) and board[newI][newJ] == "M":
                        mine_count += 1

                if mine_count > 0:
                    board[i][j] = str(mine_count)

                if mine_count == 0:
                    board[i][j] = "B"

                    for direction in directions:
                        newI = i + direction[0]
                        newJ = j + direction[1]

                        if isValid(newI, newJ, len_row, len_col) and (newI, newJ) not in visited and board[newI][newJ] == "E":
                            queue.append((newI, newJ))
                            visited.add((newI, newJ))

        return board
