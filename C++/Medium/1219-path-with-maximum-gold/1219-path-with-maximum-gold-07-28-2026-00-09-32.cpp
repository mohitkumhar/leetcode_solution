class Solution {
public:
    vector<vector<int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    int dfs(int i, int j, vector<vector<int>>& grid) {
        if (i >= grid.size() || j >= grid[0].size() || i < 0 || j < 0 ||
            grid[i][j] == 0)
            return 0;

        int maxGold = 0;

        int orgGold = grid[i][j];
        grid[i][j] = 0;

        // left, right, up, down
        for (const auto& dir : directions) {
            int newX = i + dir[0];
            int newY = j + dir[1];

            maxGold = max(maxGold, dfs(newX, newY, grid));
        }

        grid[i][j] = orgGold;

        return grid[i][j] + maxGold;
    }

    int getMaximumGold(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int maxGold = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0)
                    maxGold = max(maxGold, dfs(i, j, grid));
            }
        }
        return maxGold;
    }
};