class Solution {
public:
    int solve(int i, int j, int m, int n, vector<vector<int>>& memo) {
        if (i >= m || j >= n)
            return 0;
        if (i == m - 1 && j == n - 1)
            return 1;
        if (memo[i][j] != -1)
            return memo[i][j];

        int down = solve(i + 1, j, m, n, memo);
        int right = solve(i, j + 1, m, n, memo);

        memo[i][j] = down + right;
        return memo[i][j];
    }

    int uniquePaths(int m, int n) {
        vector<vector<int>> memo(m, vector<int>(n, -1));
        return solve(0, 0, m, n, memo);
    }
};