class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "$":
                return False

            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = "$"

            for dirx, diry in direction:
                newI = i + dirx
                newJ = j + diry

                if backtrack(newI, newJ, idx + 1):
                    return True

            board[i][j] = temp

        m = len(board)
        n = len(board[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
