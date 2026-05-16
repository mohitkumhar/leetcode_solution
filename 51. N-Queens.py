class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def is_valid(board, row, col):
            # check column for the queen
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # check upper left diagonal
            i = row 
            j = col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # check upper right diagonal
            i = row
            j = col

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row):
            if row == n:
                result.append(["".join(r) for r in board])

            if row >= n:
                return 0

            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = "Q"
                    solve(board, row + 1)
                    board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        solve(board, 0)

        return result
