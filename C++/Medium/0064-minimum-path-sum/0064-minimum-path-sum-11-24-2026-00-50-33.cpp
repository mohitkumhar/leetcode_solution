class Solution {
public:
    int m;
    int n;
    vector<vector<int>> memo;

    int solve(int i, int j, vector<vector<int>>& grid) {
        if (i >= m || j >= n) {
            return INT_MAX;
        }
        if (i == m - 1 && j == n - 1) {
            return grid[i][j];
        }
        if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int right = solve(i, j + 1, grid);
        int down = solve(i + 1, j, grid);

        return memo[i][j] = grid[i][j] + min({right, down});
    }

    int minPathSum(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        memo.assign(m, vector<int>(n, -1));

        return solve(0, 0, grid);
    }
};