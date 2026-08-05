class Solution {
public:
    void setRowZero(int row, int n, vector<vector<int>>& matrix) {
        for (int i = 0; i < n; i++)
            matrix[row][i] = 0;
    }

    void setColZero(int col, int m, vector<vector<int>>& matrix) {
        for (int i = 0; i < m; i++)
            matrix[i][col] = 0;
    }
    void setZeroes(vector<vector<int>>& matrix) {

        int m = matrix.size();
        int n = matrix[0].size();

        unordered_set<int> rows;
        unordered_set<int> cols;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 0) {
                    rows.insert(i);
                    cols.insert(j);
                }

        for (int row : rows)
            setRowZero(row, n, matrix);
        for (int col : cols)
            setColZero(col, m, matrix);
    }
};