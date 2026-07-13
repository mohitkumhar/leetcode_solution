class Solution {
public:
    int solve(int i, int j, int m, int n, vector<vector<int>>& grid,
              vector<vector<int>>& memo) {
        if (i >= m || j >= n) {
            return INT_MAX;
        } else if (i == m - 1 && j == n - 1) {
            if (grid[i][j] < 0) {
                return abs(grid[i][j]) + 1;
            } else {
                return 1;
            }
        } else if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int down = solve(i + 1, j, m, n, grid, memo);
        int right = solve(i, j + 1, m, n, grid, memo);

        if (min(down, right) - grid[i][j] <= 0) {
            memo[i][j] = 1;
        } else {
            memo[i][j] = min(down, right) - grid[i][j];
        }
        return memo[i][j];
    }

    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int>> memo(m, vector<int>(n, -1));

        return solve(0, 0, m, n, dungeon, memo);
    }
};