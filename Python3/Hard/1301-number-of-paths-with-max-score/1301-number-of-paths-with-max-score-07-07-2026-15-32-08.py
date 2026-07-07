class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 7 + 10 ** 9
        n = len(board)
        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

        dp[0][0] = (0, 1)

        for i in range(n):
            for j in range(n):
                if board[i][j] == "X" or (i == 0 and j == 0):
                    continue

                # up
                up_score, up_path = dp[i - 1][j] if i > 0 else (0, 0)
                # left
                left_score, left_path = dp[i][j - 1] if j > 0 else (0, 0)
                # diag
                diag_score, diag_path = dp[i - 1][j - 1] if i > 0 and j > 0 else (0, 0)

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

                else:
                    best_score = up_score
                    best_path = up_path

                    if left_score > best_score or left_score == best_score and left_path > best_path:
                        best_score = left_score
                        best_path = left_path

                    if diag_score > best_score or diag_score == best_score and diag_path > best_path:
                        best_score = diag_score
                        best_path = diag_path

                curr_score = 0 if board[i][j] in "SE" else int(board[i][j])
                dp[i][j] = (best_score + curr_score, best_path % MOD)

        return [0,0] if dp[n-1][n-1][1] == 0 else dp[n - 1][n - 1]
