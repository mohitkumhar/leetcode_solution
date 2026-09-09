class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(8):
            for col in range(8):
                if board[row][col] == "R":
                    r, c = row, col

        ans = 0
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        for direction in directions:
            newR = r + direction[0]
            newC = c + direction[1]

            while 0 <= newR < 8 and 0 <= newC < 8:
                if board[newR][newC] == "B":
                    break
                if board[newR][newC] == "p":
                    ans += 1
                    break

                newR = newR + direction[0]
                newC = newC + direction[1]

        return ans
