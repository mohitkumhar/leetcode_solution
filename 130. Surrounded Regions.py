class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x, y, row, col):
            return x >= 0 and x < row and y >= 0 and y < col
        
        queue = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1  or j == n-1 or j == 0:
                    if  board[i][j] == 'O':
                        board[i][j] = 'V'
                        queue.append((i, j))

        while queue:
            boundary = queue.pop()

            for direction in directions:
                newX = boundary[0] + direction[0]
                newY = boundary[1] + direction[1]

                if isValid(newX, newY, m, n) and board[newX][newY] == 'O':
                    board[newX][newY] = 'V'
                    queue.append((newX, newY))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
