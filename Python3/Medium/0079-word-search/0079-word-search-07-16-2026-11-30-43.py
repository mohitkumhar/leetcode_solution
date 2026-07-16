class Solution:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def backtrack(
        self, i: int, j: int, idx: int, word: str, board: List[List[str]]
    ) -> bool:

        if idx == len(word):
            return True

        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] == "$"
        ):
            return False

        if board[i][j] != word[idx]:
            return False

        temp = board[i][j]
        board[i][j] = "$"

        for dirx, diry in self.directions:
            newI = i + dirx
            newJ = j + diry

            if self.backtrack(newI, newJ, idx + 1, word, board):
                return True

        board[i][j] = temp

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.backtrack(i, j, 0, word, board):
                    return True
        return False
