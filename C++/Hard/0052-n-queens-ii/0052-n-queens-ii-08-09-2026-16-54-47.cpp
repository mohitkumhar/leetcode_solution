class Solution {
public:
    int result = 0;

    bool isValid(vector<vector<char>>& board, int row, int col, int n) {
        // check for queen in row
        for (int i = 0; i < n; i++)
            if (board[i][col] == 'Q')
                return false;

        // check for left diagonal
        int i = row;
        int j = col;

        while (i >= 0 && j >= 0) {
            if (board[i][j] == 'Q')
                return false;
            i--;
            j--;
        }

        // check for right diagonal

        i = row;
        j = col;

        while (i >= 0 && j < n) {
            if (board[i][j] == 'Q')
                return false;
            i--;
            j++;
        }
        return true;
    }

    void solve(vector<vector<char>>& board, int row, int n) {
        if (row >= n) {
            result++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col, n)) {
                board[row][col] = 'Q';
                solve(board, row + 1, n);
                board[row][col] = '.';
            }
        }
    }

    int totalNQueens(int n) {

        vector<vector<char>> board(n, vector<char>(n, '.'));

        solve(board, 0, n);
        return result;
    }
};