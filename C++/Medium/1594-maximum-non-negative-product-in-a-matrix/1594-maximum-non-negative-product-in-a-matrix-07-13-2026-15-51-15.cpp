class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        const int MOD = 1e9 + 7;

        vector<vector<pair<long long, long long>>> memo(
            m, vector<pair<long long, long long>>(n, {LLONG_MIN, LLONG_MAX}));

        vector<vector<pair<long long, long long>>> dp(
            m, vector<pair<long long, long long>>(n, {0, 0}));

        dp[0][0] = {grid[0][0], (long long)grid[0][0]};

        for (int i = 1; i < m; i++) {
            dp[i][0] = {dp[i - 1][0].first * (long long)grid[i][0],
                        dp[i - 1][0].second * (long long)grid[i][0]};
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = {dp[0][j - 1].first * (long long)grid[0][j],
                        dp[0][j - 1].second * (long long)grid[0][j]};
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                long long topMax = max(dp[i - 1][j].first * grid[i][j],
                                       dp[i - 1][j].second * grid[i][j]);
                long long topMin = min(dp[i - 1][j].first * grid[i][j],
                                       dp[i - 1][j].second * grid[i][j]);

                long long leftMax = max(dp[i][j - 1].first * grid[i][j],
                                        dp[i][j - 1].second * grid[i][j]);
                long long leftMin = min(dp[i][j - 1].first * grid[i][j],
                                        dp[i][j - 1].second * grid[i][j]);

                dp[i][j].first = max(topMax, leftMax);
                dp[i][j].second = min(topMin, leftMin);
            }
        }

        if (dp[m - 1][n - 1].first >= 0) {
            return dp[m - 1][n - 1].first % MOD;
        } else {
            return -1;
        }
    }
};