class Solution:
    def totalNQueens(self, n: int) -> int:

        def isValid(board, row, col):
            # check for col
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # check for left diagonal
            i = row
            j = col

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # check for right diagonal
            i = row
            j = col

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row):
            nonlocal result

            if row == n:
                result += 1
                return

            for col in range(n):
                if isValid(board, row, col):
                    board[row][col] = "Q"
                    solve(board, row + 1)
                    board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        result = 0
        solve(board, 0)

        return result
