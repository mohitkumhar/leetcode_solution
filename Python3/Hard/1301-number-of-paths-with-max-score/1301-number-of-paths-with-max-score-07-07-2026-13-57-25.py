class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 7 + 10 ** 9
        def solve(i, j):
            if i < 0 or j < 0:
                return 0, 0
            if board[i][j] == "E":
                return 0, 1
            if board[i][j] == "X":
                return 0, 0

            if memo[i][j] != -1:
                return memo[i][j]

            up_score, up_path = solve(i - 1, j)

            left_score, left_path = solve(i, j - 1)

            diag_score, diag_path = solve(i - 1, j - 1)

            
            if up_score == left_score == diag_score:
                best_score = up_score
                best_path = up_path + left_path + diag_path

            elif up_score == left_score:
                best_score = up_score
                best_path = up_path + left_path

                if diag_score > best_score or diag_score == best_score and diag_path > best_path:
                    best_score = diag_score
                    best_path = diag_path
            
            elif left_score == diag_score:
                best_score = left_score
                best_path = left_path + diag_path

                if up_score > best_score or up_score == best_score and up_path > best_path:
                    best_score = up_score
                    best_path = up_path
            
            elif up_score == diag_score:
                best_score = up_score
                best_path = up_path + diag_path

                if left_score > best_score or left_score == best_score and left_path > best_path:
                    best_score = left_score
                    best_path = left_path
            
            else: # all score are diff
                best_score = up_score
                best_path = up_path

                if left_score > best_score or left_score == best_score and left_path > best_path:
                    best_score = left_score
                    best_path = left_path

                if diag_score > best_score or diag_score == best_score and diag_path > best_path:
                    best_score = diag_score
                    best_path = diag_path

            curr_score = 0 if board[i][j] == "S" else int(board[i][j])

            memo[i][j] = best_score + curr_score, best_path % MOD
            return memo[i][j]

        n = len(board)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        best_score, best_path = solve(n - 1, n - 1)

        return [best_score, best_path] if best_path > 0 else [0, 0]
