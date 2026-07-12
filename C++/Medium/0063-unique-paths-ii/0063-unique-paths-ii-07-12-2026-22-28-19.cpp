class Solution {
public:
    int solve(int i, int j, int m, int n, vector<vector<int>> grid, vector<vector<int>> &memo) {
        if (i >= m || j >= n) {
            return 0;
        } else if (grid[i][j] == 1) {
            return 0;
        } else if (i == m - 1 && j == n - 1) {
            return 1;
        } else if (memo[i][j] != -1) {
            return memo[i][j];
        }
        int down = solve(i + 1, j, m, n, grid, memo);
        int right = solve(i, j + 1, m, n, grid, memo);

        memo[i][j] = down + right;
        return memo[i][j];
    }

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));

        return solve(0, 0, m, n, obstacleGrid, memo);
    }
};