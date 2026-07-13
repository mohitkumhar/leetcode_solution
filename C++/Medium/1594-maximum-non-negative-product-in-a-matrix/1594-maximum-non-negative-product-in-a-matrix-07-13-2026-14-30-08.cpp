class Solution {
public:
    pair<long long, long long>
    solve(int i, int j, int m, int n, vector<vector<int>>& grid,
          vector<vector<pair<long long, long long>>>& memo) {
        if (i == m - 1 && j == n - 1) {
            return {grid[i][j], grid[i][j]};
        }

        if (memo[i][j].first != LLONG_MIN && memo[i][j].second != LLONG_MAX) {
            return memo[i][j];
        }

        long long maxVal = INT_MIN;
        long long minVal = INT_MAX;

        if (i + 1 < m) {
            auto [downMax, downMin] = solve(i + 1, j, m, n, grid, memo);
            maxVal =
                max(maxVal, max(downMax * grid[i][j], downMin * grid[i][j]));
            minVal =
                min(minVal, min(downMax * grid[i][j], downMin * grid[i][j]));
        }

        if (j + 1 < n) {
            auto [rightMax, rightMin] = solve(i, j + 1, m, n, grid, memo);
            maxVal =
                max(maxVal, max(rightMax * grid[i][j], rightMin * grid[i][j]));
            minVal =
                min(minVal, min(rightMax * grid[i][j], rightMin * grid[i][j]));
        }

        memo[i][j] = {maxVal, minVal};
        return memo[i][j];
    }

    int maxProductPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int MOD = 1e9 + 7;

        vector<vector<pair<long long, long long>>> memo(
            m, vector<pair<long long, long long>>(n, {LLONG_MIN, LLONG_MAX}));

        auto [ma, _] = solve(0, 0, m, n, grid, memo);
        if (ma >= 0) {
            return ma % MOD;
        } else {
            return -1;
        }
    }
};