class Solution {
public:
    int start_i = 0;
    int start_j = 0;
    int m = 0;
    int n = 0;
    int empty_cell = 0;
    int count = 0;
    vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    void backtrack(int i, int j, int curr_cell, vector<vector<int>> grid) {
        if (i < 0 || j < 0 || i >= m || j >= n) {
            return;
        }
        if (grid[i][j] == 2) {
            if (curr_cell == empty_cell) {
                count++;
                return;
            }
        } else if (grid[i][j] == -1) {
            return;
        }

        grid[i][j] = -1;
        for (auto& d : directions) {
            int ni = i + d[0];
            int nj = j + d[1];
            curr_cell++;
            backtrack(ni, nj, curr_cell, grid);
            curr_cell--;
        }
        grid[i][j] = 0;
    }

    int uniquePathsIII(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    start_i = i;
                    start_j = j;
                }
                if (grid[i][j] == 0) {
                    empty_cell++;
                }
            }
        }
        empty_cell++;
        backtrack(start_i, start_j, 0, grid);

        return count;
    }
};