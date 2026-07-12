class Solution {
public:
    int solve(int i, int j, int m, int n, vector<vector<int>>& grid,
              vector<vector<int>>& memo) {
        if (i >= m || j >= n) {
            return INT_MAX;
        } else if (i == m - 1 && j == n - 1) {
            return grid[i][j];
        } else if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int down = solve(i + 1, j, m, n, grid, memo);
        int right = solve(i, j + 1, m, n, grid, memo);

        memo[i][j] = min(down, right) + grid[i][j];
        return memo[i][j];
    }

    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = grid[0][0];

        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }

        return dp[m - 1][n - 1];
    }
};